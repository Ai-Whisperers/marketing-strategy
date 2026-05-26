"""
Carrusel Instagram 1080×1350 (4:5) — planes ParaguAI (feed).

Colores tomados del CSS público de paragu-ai.com (Tailwind: slate-900 / slate-800,
purple-500 #a855f7 → pink-500 #ec4899). Nombres de planes alineados a la web:
Starter, Profesional, Negocio + cierre plan a medida.

Plantilla tipo **anuncio**: imagen o gráfico procedural a **pantalla completa** dentro de la tarjeta
redondeada (`side-NN.png` opcional), velo oscuro para contraste, copy centrado a ancho completo
(sin columna derecha). CTA + logo en franja inferior.

  pip install -r scripts/requirements-creativos.txt
  python scripts/build_carousel_planes_png.py
  python scripts/build_carousel_planes_png.py --layout-debug
    → escribe paraguai-carousel-planes-0N-layout-debug.png (no pisa los finales).

Solo usa Pillow (requirements-creativos.txt). `--layout-debug` dibuja contornos
de zonas (texto / CTA / logo) para revisar composición sin otras herramientas.

Opcional: brand/fonts/*.ttf o PARAGUAI_FONT_DIR. Orden de fuentes alineado a brand/TYPOGRAPHY-POST-STANDARD-es.md.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import NamedTuple

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

W = 1080
H = 1350

# paragu-ai.com — chunk CSS Next (Tailwind): slate-900, purple-500, pink-500
NAVY = (15, 23, 42)
CARD = (30, 41, 59)
CARD_INNER = (15, 23, 42)
CARD_BORDER = (71, 85, 105)
WHITE = (255, 255, 255)
LAVENDER = (216, 180, 254)
LAVENDER_MUTED = (196, 181, 253)
MUTED = (148, 163, 184)
ACCENT_HOT = (192, 132, 252)
GRAD_LEFT = (168, 85, 247)
GRAD_RIGHT = (236, 72, 153)
GOLD = (251, 191, 36)
GOLD_DARK = (120, 53, 15)

CARD_PAD = 48
CARD_TOP_INSET = 40
CARD_RADIUS = 38
SHADOW_OFFSET = (10, 18)
SHADOW_BLUR = 28
SHADOW_ALPHA = 95

AD_TEXT_MARGIN = 56
TEXT_ALIGN = "center"
MIN_TEXT_GAP = 12
GAP_AFTER_TALL_LINE = 8
TEXT_VERTICAL_BIAS = 0.32
TEXT_WRAP_PAD = 8
LOGO_BOTTOM_INSET = 22
LOGO_MAX_HEIGHT = 56
GAP_CTA_TO_LOGO = 14
GAP_TEXT_TO_CTA = 28
HEADLINE_TO_SUBTITLE_EXTRA_GAP = 28
LAYOUT_DEBUG = False


class TextRow(NamedTuple):
    """Una fila de copy: role headline|subtitle|label|body|price; gap_before suma px antes de la fila."""

    text: str
    size: int
    bold: bool
    rgb: tuple[int, int, int]
    outline: bool = False
    gap_before: int = 0
    role: str = "body"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def side_image_dir() -> Path:
    return repo_root() / "assets" / "creativos" / "carousel-planes"


def font_search_dirs() -> list[Path]:
    dirs: list[Path] = []
    env = os.environ.get("PARAGUAI_FONT_DIR")
    if env:
        dirs.append(Path(env))
    dirs.append(repo_root() / "brand" / "fonts")
    windir = os.environ.get("WINDIR", "C:/Windows")
    dirs.append(Path(windir) / "Fonts")
    return dirs


def _load_font_from_dirs(size: int, names: tuple[str, ...]) -> ImageFont.FreeTypeFont | None:
    for base in font_search_dirs():
        if not base.is_dir():
            continue
        for name in names:
            p = base / name
            if p.is_file():
                try:
                    return ImageFont.truetype(str(p), size)
                except OSError:
                    continue
        if base.name == "fonts":
            for p in sorted(base.glob("*.ttf")):
                try:
                    return ImageFont.truetype(str(p), size)
                except OSError:
                    continue
    return None


def pick_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    preferred_bold = (
        "inter-bold.ttf",
        "Inter-Bold.ttf",
        "Inter_18pt-Bold.ttf",
        "PlusJakartaSans-Bold.ttf",
        "DMSans-Bold.ttf",
        "DM-Sans-Bold.ttf",
        "Montserrat-Bold.ttf",
        "segoeuib.ttf",
        "segoeui.ttf",
        "arialbd.ttf",
        "arial.ttf",
    )
    preferred_regular = (
        "inter-regular.ttf",
        "Inter-Regular.ttf",
        "Inter_18pt-Regular.ttf",
        "PlusJakartaSans-Regular.ttf",
        "DMSans-Regular.ttf",
        "DM-Sans-Regular.ttf",
        "Montserrat-Regular.ttf",
        "segoeui.ttf",
        "arial.ttf",
    )
    names = preferred_bold if bold else preferred_regular
    hit = _load_font_from_dirs(size, names)
    if hit is not None:
        return hit
    return ImageFont.load_default()


def pick_font_subtitle(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    preferred = (
        "inter-medium.ttf",
        "Inter-Medium.ttf",
        "Inter_18pt-Medium.ttf",
        "PlusJakartaSans-Medium.ttf",
        "DMSans-Medium.ttf",
        "DM-Sans-Medium.ttf",
        "Montserrat-Medium.ttf",
        "inter-semibold.ttf",
        "Inter-SemiBold.ttf",
        "Inter_18pt-SemiBold.ttf",
        "PlusJakartaSans-SemiBold.ttf",
        "DMSans-SemiBold.ttf",
        "DM-Sans-SemiBold.ttf",
        "Montserrat-SemiBold.ttf",
        "inter-regular.ttf",
        "Inter-Regular.ttf",
        "Inter_18pt-Regular.ttf",
        "PlusJakartaSans-Regular.ttf",
        "DMSans-Regular.ttf",
        "DM-Sans-Regular.ttf",
        "Montserrat-Regular.ttf",
        "segoeui.ttf",
        "arial.ttf",
    )
    hit = _load_font_from_dirs(size, preferred)
    if hit is not None:
        return hit
    return pick_font(size, bold=False)


def pick_font_for_row(
    size: int, bold: bool, role: str
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if role == "subtitle":
        return pick_font_subtitle(size)
    if role == "label":
        return pick_font_subtitle(size)
    if role == "body":
        return pick_font(size, bold=bold)
    if role == "price":
        return pick_font(size, bold=True)
    return pick_font(size, bold=bold)


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def _font_px(font: ImageFont.ImageFont) -> int:
    if hasattr(font, "size"):
        return int(getattr(font, "size", 0))
    return 0


def draw_text_outlined(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    *,
    outline: tuple[int, int, int] = (10, 14, 28),
    width: int = 2,
) -> None:
    x, y = xy
    rgba_fill = (*fill, 255)
    rgba_ol = (*outline, 255)
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill=rgba_ol)
    draw.text((x, y), text, font=font, fill=rgba_fill)


def make_background_rgba() -> Image.Image:
    base = Image.new("RGBA", (W, H), (*NAVY, 255))
    blobs = [
        (130, 180, 450, (*GRAD_LEFT, 34)),
        (980, 280, 410, (*GRAD_RIGHT, 28)),
        (540, 1180, 520, (*GRAD_LEFT, 24)),
        (900, 1080, 320, (59, 130, 246, 16)),
    ]
    for cx, cy, r, rgba in blobs:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(layer).ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgba)
        base = Image.alpha_composite(base, layer)
    return base


def composite_rounded_shadow(
    canvas: Image.Image,
    xy: tuple[int, int, int, int],
    radius: int,
) -> Image.Image:
    x0, y0, x1, y1 = xy
    sx, sy = SHADOW_OFFSET
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(
        [x0 + sx, y0 + sy, x1 + sx, y1 + sy],
        radius=radius,
        fill=(0, 0, 0, SHADOW_ALPHA),
    )
    layer = layer.filter(ImageFilter.GaussianBlur(SHADOW_BLUR))
    return Image.alpha_composite(canvas, layer)


def draw_card_border_rim(canvas: Image.Image, xy: tuple[int, int, int, int], radius: int) -> None:
    x0, y0, x1, y1 = xy
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle(
        [x0, y0, x1, y1],
        radius=radius,
        outline=(*CARD_BORDER, 255),
        width=2,
    )
    rim = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ir = max(8, radius - 2)
    ImageDraw.Draw(rim).rounded_rectangle(
        [x0 + 2, y0 + 2, x1 - 2, y1 - 2],
        radius=ir,
        outline=(255, 255, 255, 36),
        width=1,
    )
    canvas.alpha_composite(rim)


def lerp_rgb(
    a: tuple[int, int, int], b: tuple[int, int, int], t: float
) -> tuple[int, int, int]:
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
    )


def draw_gradient_cta_pill(
    canvas: Image.Image,
    text: str,
    font: ImageFont.ImageFont,
    cx: int,
    cy: int,
) -> None:
    if canvas.mode != "RGBA":
        raise ValueError("draw_gradient_cta_pill requires RGBA canvas")
    d = ImageDraw.Draw(canvas)
    tw, th = text_size(d, text, font)
    pad_x, pad_y = 36, 22
    w, h = tw + 2 * pad_x, th + 2 * pad_y
    r = max(16, h // 2)
    x0, y0 = cx - w // 2, cy - h // 2
    grad = Image.new("RGB", (w, h), (0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for i in range(w):
        t = i / max(w - 1, 1)
        gd.line([(i, 0), (i, h - 1)], fill=lerp_rgb(GRAD_LEFT, GRAD_RIGHT, t))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=255)
    pill = Image.merge("RGBA", (*grad.split(), mask))
    canvas.paste(pill, (x0, y0), pill)
    tx, ty = x0 + pad_x, y0 + pad_y - 2
    d2 = ImageDraw.Draw(canvas)
    d2.text((tx + 1, ty + 1), text, font=font, fill=(12, 10, 20, 140))
    d2.text((tx, ty), text, font=font, fill=(*WHITE, 255))


def draw_corner_planes_label(canvas: Image.Image, x0: int, y0: int) -> None:
    text = "Planes"
    font = pick_font(16, bold=True)
    d = ImageDraw.Draw(canvas)
    tw, th = text_size(d, text, font)
    pad_x, pad_y = 12, 6
    w, h = tw + 2 * pad_x, th + 2 * pad_y
    lx, ly = x0 + 8, y0 + 8
    d.rounded_rectangle(
        [lx, ly, lx + w, ly + h],
        radius=h // 2,
        fill=(*CARD_INNER, 255),
        outline=(*CARD_BORDER, 220),
        width=1,
    )
    d.text((lx + pad_x, ly + pad_y - 2), text, font=font, fill=(*MUTED, 255))


def draw_badge_mas_elegido(canvas: Image.Image, cx: int, y: int, font: ImageFont.ImageFont) -> None:
    text = "Más elegido"
    d = ImageDraw.Draw(canvas)
    tw, th = text_size(d, text, font)
    pad_x, pad_y = 18, 8
    w, h = tw + 2 * pad_x, th + 2 * pad_y
    x0, y0 = cx - w // 2, y - h // 2
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=12, fill=(*GOLD, 255), outline=(*GOLD_DARK, 255), width=2)
    d.text((x0 + pad_x, y0 + pad_y - 1), text, font=font, fill=(30, 20, 5, 255))


def hard_break_long_token(
    d: ImageDraw.ImageDraw,
    line: str,
    font: ImageFont.ImageFont,
    max_width: int,
) -> list[str]:
    if max_width <= 16:
        return [line]
    tw, _ = text_size(d, line, font)
    if tw <= max_width:
        return [line]
    out: list[str] = []
    chunk = ""
    for ch in line:
        trial = chunk + ch
        tt, _ = text_size(d, trial, font)
        if tt <= max_width or not chunk:
            chunk = trial
        else:
            out.append(chunk)
            chunk = ch
    if chunk:
        out.append(chunk)
    return out if out else [line]


def expand_overwide_lines(
    d: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.ImageFont,
    max_width: int,
) -> list[str]:
    fixed: list[str] = []
    for ln in lines:
        tw, _ = text_size(d, ln, font)
        if tw <= max_width:
            fixed.append(ln)
        else:
            fixed.extend(hard_break_long_token(d, ln, font, max_width))
    return fixed


def wrap_line_to_width(
    d: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.ImageFont,
    max_width: int,
) -> list[str]:
    text = text.strip()
    if not text or max_width <= 16:
        return [text] if text else [""]
    tw, _ = text_size(d, text, font)
    if tw <= max_width:
        return [text]
    words = text.split()
    if len(words) <= 1:
        line = words[0] if words else text
        twl, _ = text_size(d, line, font)
        if twl <= max_width:
            return [line]
        return hard_break_long_token(d, line, font, max_width)
    lines: list[str] = []
    cur = words[0]
    for w in words[1:]:
        trial = f"{cur} {w}"
        ttw, _ = text_size(d, trial, font)
        if ttw <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return expand_overwide_lines(d, lines, font, max_width)


def iter_wrapped_stack(
    rows: list[TextRow],
    delta: int,
    d: ImageDraw.ImageDraw,
    max_width: int,
) -> list[tuple[TextRow, str, ImageFont.ImageFont, int, bool]]:
    """Líneas finales (con wrap), altura y si es la primera línea del TextRow."""
    out: list[tuple[TextRow, str, ImageFont.ImageFont, int, bool]] = []
    for row in rows:
        sz = max(14, row.size + delta)
        font = pick_font_for_row(sz, row.bold, row.role)
        first = True
        for raw in row.text.split("\n"):
            for line in wrap_line_to_width(d, raw, font, max_width):
                if not line:
                    continue
                _, th = text_size(d, line, font)
                out.append((row, line, font, th, first))
                first = False
    return out


def _stack_line_leading(
    row: TextRow,
    first_in_row: bool,
    prev_row: TextRow | None,
    gap: int,
    prev_line_th: int,
) -> int:
    """Espacio vertical entre la línea anterior y esta (incl. gap estándar)."""
    extra = gap
    if prev_line_th >= 34:
        extra += GAP_AFTER_TALL_LINE
    if first_in_row:
        extra += row.gap_before
        if (
            prev_row is not None
            and prev_row.role == "headline"
            and row.role == "subtitle"
        ):
            extra += HEADLINE_TO_SUBTITLE_EXTRA_GAP
    return extra


def measure_wrapped_stack_height(
    rows: list[TextRow], delta: int, gap: int, max_width: int
) -> int:
    tmp = Image.new("RGBA", (W, 2400), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    lines = iter_wrapped_stack(rows, delta, d, max_width)
    if not lines:
        return 0
    y = 0
    prev_row: TextRow | None = None
    prev_th = 0
    for i, (row, _, _, th, first_in_row) in enumerate(lines):
        if i > 0:
            y += _stack_line_leading(row, first_in_row, prev_row, gap, prev_th)
        y += th
        prev_row = row
        prev_th = th
    return y


def draw_text_stack_top(
    canvas: Image.Image,
    rows: list[TextRow],
    left: int,
    top: int,
    right: int,
    bottom: int,
    *,
    delta: int = 0,
    gap: int = MIN_TEXT_GAP,
    outline_from_px: int = 36,
    align: str = "left",
) -> int:
    """Dibuja bloques con wrap; align 'center' o 'left'."""
    d = ImageDraw.Draw(canvas)
    max_w = max(40, right - left - TEXT_WRAP_PAD)
    y = float(top)
    lines = iter_wrapped_stack(rows, delta, d, max_w)
    prev_row: TextRow | None = None
    prev_th = 0
    for i, (row, part, font, th, first_in_row) in enumerate(lines):
        if i > 0:
            y += _stack_line_leading(row, first_in_row, prev_row, gap, prev_th)
        if y > bottom:
            return int(y)
        tw, th2 = text_size(d, part, font)
        th = th2
        if align == "center":
            x = (left + right - tw) // 2
        else:
            x = left
        use_outline = (
            row.role == "headline"
            and row.outline
            and _font_px(font) >= outline_from_px
        )
        if use_outline:
            draw_text_outlined(
                d, (x, int(y)), part, font, row.rgb, outline=(12, 18, 36), width=2
            )
        else:
            d.text((x, int(y)), part, font=font, fill=(*row.rgb, 255))
        y += th
        prev_row = row
        prev_th = th
    return int(y)


def fit_and_draw_text_column(
    canvas: Image.Image,
    rows: list[TextRow],
    left: int,
    top: int,
    right: int,
    bottom: int,
    *,
    align: str = TEXT_ALIGN,
) -> int:
    """Dibuja el bloque de copy; devuelve la Y donde empezó (útil para layout-debug)."""
    gap = MIN_TEXT_GAP
    max_w = max(40, right - left - TEXT_WRAP_PAD)
    avail = max(1, bottom - top)
    chosen_delta = -18
    for delta in range(22, -21, -2):
        h = measure_wrapped_stack_height(rows, delta, gap, max_w)
        if h <= avail:
            chosen_delta = delta
            break
    h = measure_wrapped_stack_height(rows, chosen_delta, gap, max_w)
    slack = max(0, avail - h)
    y_start = top + int(slack * TEXT_VERTICAL_BIAS)
    draw_text_stack_top(
        canvas,
        rows,
        left,
        y_start,
        right,
        bottom,
        delta=chosen_delta,
        gap=gap,
        align=align,
    )
    return y_start


def draw_procedural_side(
    target: Image.Image,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    slide: int,
) -> None:
    w, h = x1 - x0, y1 - y0
    if w <= 0 or h <= 0:
        return
    panel = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel)
    pr = 24
    pd.rounded_rectangle([0, 0, w - 1, h - 1], radius=pr, fill=(*CARD_INNER, 240), outline=(*CARD_BORDER, 255), width=1)

    if slide == 1:
        bar_h = max(36, h // 8)
        for i in range(w):
            t = i / max(w - 1, 1)
            pd.line([(i, 12), (i, 12 + bar_h)], fill=lerp_rgb(GRAD_LEFT, GRAD_RIGHT, t))
        ly = 12 + bar_h + 18
        for i in range(5):
            bw = int(w * (0.55 - i * 0.08))
            pd.rounded_rectangle([16, ly, 16 + bw, ly + 10], radius=5, fill=(255, 255, 255, 35))
            ly += 22
    elif slide == 2:
        pd.ellipse([w // 2 - 48, h // 2 - 70, w // 2 + 48, h // 2 + 26], outline=(*LAVENDER, 200), width=3)
        pd.ellipse([w // 2 - 18, h // 2 - 42, w // 2 + 18, h // 2 - 12], fill=(*WHITE, 90))
        pd.rounded_rectangle([14, h - 120, w - 14, h - 24], radius=12, fill=(255, 255, 255, 18))
    elif slide == 3:
        cx, cy = w // 2, h // 3
        pd.ellipse([cx - 40, cy - 40, cx + 40, cy + 40], fill=(*lerp_rgb(GRAD_LEFT, GRAD_RIGHT, 0.4), 180))
        pd.polygon(
            [(cx + 50, cy + 20), (cx + 50, cy + 70), (cx + 10, cy + 45)],
            fill=(*GRAD_RIGHT, 220),
        )
        pd.rounded_rectangle([12, h - 100, w - 12, h - 20], radius=10, fill=(255, 255, 255, 14))
    elif slide == 4:
        gw = (w - 40) // 3
        gy = h // 3
        for i in range(3):
            pd.rounded_rectangle([20 + i * (gw + 8), gy, 20 + i * (gw + 8) + gw, gy + gw], radius=8, fill=(255, 255, 255, 20))
        pd.rounded_rectangle([16, h - 90, w - 16, h - 22], radius=14, fill=(*GRAD_LEFT, 60))
    else:
        for i in range(3):
            px = 20 + i * (w - 50) // 3
            pd.rounded_rectangle([px, h // 2 - 20, px + 56, h // 2 + 60], radius=8, fill=(255, 255, 255, 22))

    target.paste(panel, (x0, y0), panel)


def paint_ad_template_backdrop(
    canvas: Image.Image,
    inner: tuple[int, int, int, int],
    slide_index: int,
) -> None:
    """Fondo tipo anuncio: side-NN.png a pantalla completa en la tarjeta o procedural + velo."""
    x0, y0, x1, y1 = inner
    w = x1 - x0
    h = y1 - y0
    if w <= 1 or h <= 1:
        return
    block = Image.new("RGBA", (w, h), (*CARD, 255))
    path = side_image_dir() / f"side-{slide_index:02d}.png"
    if path.is_file():
        img = Image.open(path).convert("RGBA")
        img = ImageOps.fit(img, (w, h), Image.Resampling.LANCZOS)
        block.paste(img, (0, 0), img)
    else:
        draw_procedural_side(block, 0, 0, w - 1, h - 1, slide_index)
    veil = Image.new("RGBA", (w, h), (10, 14, 28, 138))
    block = Image.alpha_composite(block, veil)
    rr = max(6, CARD_RADIUS - 1)
    rmask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(rmask).rounded_rectangle(
        [0, 0, w - 1, h - 1],
        radius=rr,
        fill=255,
    )
    canvas.paste(block, (x0, y0), rmask)


def cta_pill_total_height(cta_text: str, font_px: int) -> int:
    tmp = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    font = pick_font(font_px, True)
    _, th = text_size(d, cta_text, font)
    pad_y = 22
    return th + 2 * pad_y


def compute_footer_placements(
    y0: int,
    y1: int,
    logo_path: Path,
    band_left: int,
    band_right: int,
    cta_text: str,
    cta_font_px: int,
) -> tuple[int, int, Image.Image, int, int]:
    """text_bottom, cta_cy, logo_rgba, logo_x, logo_y_top."""
    pill_h = cta_pill_total_height(cta_text, cta_font_px)
    half = pill_h // 2
    band_w = max(80, band_right - band_left)
    raw = Image.open(logo_path).convert("RGBA")
    min_text_bottom = y0 + 140
    nh = LOGO_MAX_HEIGHT
    text_bottom = min_text_bottom
    cy_cta = y1 - 120
    logo_img = raw
    logo_x = band_left
    y_logo_top = y1 - LOGO_BOTTOM_INSET - nh

    while nh >= 26:
        nw = int(raw.width * nh / raw.height)
        if nw > band_w:
            nw = band_w
            nh = int(raw.height * nw / raw.width)
        y_logo_bottom = y1 - LOGO_BOTTOM_INSET
        y_logo_top = y_logo_bottom - nh
        cy_cta = y_logo_top - GAP_CTA_TO_LOGO - half
        text_bottom = int(cy_cta - half - GAP_TEXT_TO_CTA)
        if text_bottom >= min_text_bottom:
            logo_img = raw.resize((nw, nh), Image.Resampling.LANCZOS)
            logo_x = (band_left + band_right - nw) // 2
            return text_bottom, cy_cta, logo_img, logo_x, y_logo_top
        nh -= 8

    nw = int(raw.width * 26 / raw.height)
    nw = min(nw, band_w)
    nh = int(raw.height * nw / raw.width)
    logo_img = raw.resize((nw, nh), Image.Resampling.LANCZOS)
    y_logo_bottom = y1 - LOGO_BOTTOM_INSET
    y_logo_top = y_logo_bottom - nh
    cy_cta = y_logo_top - GAP_CTA_TO_LOGO - half
    text_bottom = int(cy_cta - half - GAP_TEXT_TO_CTA)
    logo_x = (band_left + band_right - nw) // 2
    return text_bottom, cy_cta, logo_img, logo_x, y_logo_top


def draw_footer_branding(
    canvas: Image.Image,
    logo_rgba: Image.Image,
    *,
    cta_text: str,
    cta_font_px: int,
    mid_x: int,
    cta_cy: int,
    logo_xy: tuple[int, int],
) -> None:
    draw_gradient_cta_pill(
        canvas, cta_text, pick_font(cta_font_px, True), mid_x, cta_cy
    )
    canvas.paste(logo_rgba, logo_xy, logo_rgba)


def draw_layout_debug(
    canvas: Image.Image,
    *,
    inner: tuple[int, int, int, int],
    mid_x: int,
    text_left: int,
    text_right: int,
    text_top: int,
    text_bottom: int,
    cta_cy: int,
    cta_text: str,
    cta_font_px: int,
    logo_box: tuple[int, int, int, int],
) -> None:
    if not LAYOUT_DEBUG:
        return
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rounded_rectangle(
        [text_left, text_top, text_right, text_bottom],
        radius=4,
        outline=(0, 255, 200, 200),
        width=3,
    )
    ph = cta_pill_total_height(cta_text, cta_font_px)
    d.rounded_rectangle(
        [mid_x - 200, cta_cy - ph // 2, mid_x + 200, cta_cy + ph // 2],
        radius=8,
        outline=(255, 220, 0, 220),
        width=2,
    )
    lx0, ly0, lx1, ly1 = logo_box
    d.rectangle([lx0, ly0, lx1, ly1], outline=(255, 80, 80, 220), width=2)
    canvas.alpha_composite(overlay)


def card_inner_bounds() -> tuple[int, int, int, int]:
    x0 = CARD_PAD
    y0 = CARD_PAD + CARD_TOP_INSET
    x1 = W - CARD_PAD
    y1 = H - CARD_PAD
    return x0, y0, x1, y1


def finalize(canvas: Image.Image, out: Path) -> None:
    rgba = canvas.convert("RGBA")
    rgb = Image.new("RGB", rgba.size, NAVY)
    rgb.paste(rgba, mask=rgba.split()[3])
    rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1.0, percent=110, threshold=2))
    rgb.save(out, "PNG", optimize=True)


def build_common() -> tuple[Image.Image, tuple[int, int, int, int]]:
    canvas = make_background_rgba()
    inner = card_inner_bounds()
    canvas = composite_rounded_shadow(canvas, inner, CARD_RADIUS)
    return canvas, inner


def build_slide1(out: Path, logo_path: Path) -> None:
    canvas, inner = build_common()
    x0, y0, x1, y1 = inner
    paint_ad_template_backdrop(canvas, inner, 1)
    draw_card_border_rim(canvas, inner, CARD_RADIUS)
    band_l, band_r = x0 + 16, x1 - 16
    cta_txt, cta_px = "paragu-ai.com", 26
    text_bottom, cta_cy, logo_img, logo_x, y_logo_top = compute_footer_placements(
        y0, y1, logo_path, band_l, band_r, cta_txt, cta_px
    )
    left = x0 + AD_TEXT_MARGIN
    right = x1 - AD_TEXT_MARGIN
    top = y0 + 36
    rows = [
        TextRow("Tu negocio vendiendo", 48, True, WHITE, True, 0, "headline"),
        TextRow("mientras dormís", 48, True, LAVENDER, True, 0, "headline"),
        TextRow("Sitio profesional en 48 h", 28, False, MUTED, False, 0, "subtitle"),
        TextRow(
            "Todo incluido: diseño, dominio .com.py,\nSEO y botón WhatsApp.",
            22,
            False,
            MUTED,
            False,
            0,
            "body",
        ),
        TextRow("Demo gratis · sin tarjeta", 23, False, MUTED, False, 0, "body"),
    ]
    y_text = fit_and_draw_text_column(canvas, rows, left, top, right, text_bottom)
    mid = (x0 + x1) // 2
    draw_footer_branding(
        canvas,
        logo_img,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        mid_x=mid,
        cta_cy=cta_cy,
        logo_xy=(logo_x, y_logo_top),
    )
    draw_layout_debug(
        canvas,
        inner=inner,
        mid_x=mid,
        text_left=left,
        text_right=right,
        text_top=y_text,
        text_bottom=text_bottom,
        cta_cy=cta_cy,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        logo_box=(
            logo_x,
            y_logo_top,
            logo_x + logo_img.width,
            y_logo_top + logo_img.height,
        ),
    )
    finalize(canvas, out)


def build_slide2(out: Path, logo_path: Path) -> None:
    canvas, inner = build_common()
    x0, y0, x1, y1 = inner
    paint_ad_template_backdrop(canvas, inner, 2)
    draw_card_border_rim(canvas, inner, CARD_RADIUS)
    draw_corner_planes_label(canvas, x0, y0)
    band_l, band_r = x0 + 16, x1 - 16
    cta_txt, cta_px = "Empezar gratis", 26
    text_bottom, cta_cy, logo_img, logo_x, y_logo_top = compute_footer_placements(
        y0, y1, logo_path, band_l, band_r, cta_txt, cta_px
    )
    left = x0 + AD_TEXT_MARGIN
    right = x1 - AD_TEXT_MARGIN
    top = y0 + 44
    rows = [
        TextRow("Starter", 50, True, WHITE, True, 0, "headline"),
        TextRow("Para probar sin compromiso", 24, False, MUTED, False, 0, "subtitle"),
        TextRow("Qué incluye", 20, True, LAVENDER_MUTED, False, 0, "label"),
        TextRow(
            "• Subdominio gratis (tuNEGOCIO.paragu-ai.com)\n"
            "• Página con tus datos y botón WhatsApp\n"
            "• Probá 3 meses full antes de pagar dominio",
            20,
            False,
            MUTED,
            False,
            0,
            "body",
        ),
        TextRow("Setup: gratis · sin tarjeta", 23, True, LAVENDER, True, 0, "headline"),
    ]
    y_text = fit_and_draw_text_column(canvas, rows, left, top, right, text_bottom)
    mid = (x0 + x1) // 2
    draw_footer_branding(
        canvas,
        logo_img,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        mid_x=mid,
        cta_cy=cta_cy,
        logo_xy=(logo_x, y_logo_top),
    )
    draw_layout_debug(
        canvas,
        inner=inner,
        mid_x=mid,
        text_left=left,
        text_right=right,
        text_top=y_text,
        text_bottom=text_bottom,
        cta_cy=cta_cy,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        logo_box=(
            logo_x,
            y_logo_top,
            logo_x + logo_img.width,
            y_logo_top + logo_img.height,
        ),
    )
    finalize(canvas, out)


def build_slide3(out: Path, logo_path: Path) -> None:
    canvas, inner = build_common()
    x0, y0, x1, y1 = inner
    paint_ad_template_backdrop(canvas, inner, 3)
    draw_card_border_rim(canvas, inner, CARD_RADIUS)
    draw_corner_planes_label(canvas, x0, y0)
    band_l, band_r = x0 + 16, x1 - 16
    cta_txt, cta_px = "Elegir Profesional", 24
    text_bottom, cta_cy, logo_img, logo_x, y_logo_top = compute_footer_placements(
        y0, y1, logo_path, band_l, band_r, cta_txt, cta_px
    )
    left = x0 + AD_TEXT_MARGIN
    right = x1 - AD_TEXT_MARGIN
    top = y0 + 86
    mid_badge = (x0 + x1) // 2
    draw_badge_mas_elegido(canvas, mid_badge, y0 + 50, pick_font(18))
    rows = [
        TextRow("Profesional", 48, True, WHITE, True, 0, "headline"),
        TextRow("Tu sitio con marca propia en Paraguay", 23, False, MUTED, False, 0, "subtitle"),
        TextRow("Setup: Gs. 650.000", 32, True, LAVENDER, True, 0, "headline"),
        TextRow("+ Gs. 100.000 / mes", 28, True, WHITE, False, 0, "headline"),
        TextRow("Qué incluye", 19, True, LAVENDER_MUTED, False, 0, "label"),
        TextRow(
            "• Dominio .com.py 1 año + SSL\n"
            "• Hasta 5 páginas · Maps · SEO local\n"
            "• Formulario de contacto · 2 cambios/mes\n"
            "• Soporte por WhatsApp",
            19,
            False,
            MUTED,
            False,
            0,
            "body",
        ),
    ]
    y_text = fit_and_draw_text_column(canvas, rows, left, top, right, text_bottom)
    mid = (x0 + x1) // 2
    draw_footer_branding(
        canvas,
        logo_img,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        mid_x=mid,
        cta_cy=cta_cy,
        logo_xy=(logo_x, y_logo_top),
    )
    draw_layout_debug(
        canvas,
        inner=inner,
        mid_x=mid,
        text_left=left,
        text_right=right,
        text_top=y_text,
        text_bottom=text_bottom,
        cta_cy=cta_cy,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        logo_box=(
            logo_x,
            y_logo_top,
            logo_x + logo_img.width,
            y_logo_top + logo_img.height,
        ),
    )
    finalize(canvas, out)


def build_slide4(out: Path, logo_path: Path) -> None:
    canvas, inner = build_common()
    x0, y0, x1, y1 = inner
    paint_ad_template_backdrop(canvas, inner, 4)
    draw_card_border_rim(canvas, inner, CARD_RADIUS)
    draw_corner_planes_label(canvas, x0, y0)
    band_l, band_r = x0 + 16, x1 - 16
    cta_txt, cta_px = "Elegir Negocio", 24
    text_bottom, cta_cy, logo_img, logo_x, y_logo_top = compute_footer_placements(
        y0, y1, logo_path, band_l, band_r, cta_txt, cta_px
    )
    left = x0 + AD_TEXT_MARGIN
    right = x1 - AD_TEXT_MARGIN
    top = y0 + 44
    rows = [
        TextRow("Negocio", 48, True, WHITE, True, 0, "headline"),
        TextRow("Para vender con reservas y catálogo", 23, False, MUTED, False, 0, "subtitle"),
        TextRow("Setup: Gs. 1.200.000", 32, True, LAVENDER, True, 0, "headline"),
        TextRow("+ Gs. 150.000 / mes", 28, True, WHITE, False, 0, "headline"),
        TextRow("Qué suma respecto a Profesional", 19, True, LAVENDER_MUTED, False, 0, "label"),
        TextRow(
            "• Sistema de reservas online\n"
            "• Catálogo de hasta 20 productos + blog\n"
            "• 5 cambios/mes · soporte prioritario",
            19,
            False,
            MUTED,
            False,
            0,
            "body",
        ),
    ]
    y_text = fit_and_draw_text_column(canvas, rows, left, top, right, text_bottom)
    mid = (x0 + x1) // 2
    draw_footer_branding(
        canvas,
        logo_img,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        mid_x=mid,
        cta_cy=cta_cy,
        logo_xy=(logo_x, y_logo_top),
    )
    draw_layout_debug(
        canvas,
        inner=inner,
        mid_x=mid,
        text_left=left,
        text_right=right,
        text_top=y_text,
        text_bottom=text_bottom,
        cta_cy=cta_cy,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        logo_box=(
            logo_x,
            y_logo_top,
            logo_x + logo_img.width,
            y_logo_top + logo_img.height,
        ),
    )
    finalize(canvas, out)


def build_slide5(out: Path, logo_path: Path) -> None:
    canvas, inner = build_common()
    x0, y0, x1, y1 = inner
    paint_ad_template_backdrop(canvas, inner, 5)
    draw_card_border_rim(canvas, inner, CARD_RADIUS)
    draw_corner_planes_label(canvas, x0, y0)
    band_l, band_r = x0 + 16, x1 - 16
    cta_txt, cta_px = "Hablar con ventas", 24
    text_bottom, cta_cy, logo_img, logo_x, y_logo_top = compute_footer_placements(
        y0, y1, logo_path, band_l, band_r, cta_txt, cta_px
    )
    left = x0 + AD_TEXT_MARGIN
    right = x1 - AD_TEXT_MARGIN
    top = y0 + 42
    rows = [
        TextRow("¿Varias sucursales o equipo grande?", 34, True, WHITE, True, 0, "headline"),
        TextRow("Plan a medida", 25, False, MUTED, False, 0, "subtitle"),
        TextRow(
            "Incluye lo esencial de Negocio y escala\n"
            "a multi-sucursal / operaciones más complejas.",
            19,
            False,
            MUTED,
            False,
            0,
            "body",
        ),
        TextRow("Setup: Gs. 2.200.000", 30, True, LAVENDER, True, 0, "headline"),
        TextRow("+ Gs. 300.000 / mes", 26, True, WHITE, False, 0, "headline"),
        TextRow("Coordinamos alcance por WhatsApp.", 18, False, MUTED, False, 0, "body"),
    ]
    y_text = fit_and_draw_text_column(canvas, rows, left, top, right, text_bottom)
    mid = (x0 + x1) // 2
    draw_footer_branding(
        canvas,
        logo_img,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        mid_x=mid,
        cta_cy=cta_cy,
        logo_xy=(logo_x, y_logo_top),
    )
    draw_layout_debug(
        canvas,
        inner=inner,
        mid_x=mid,
        text_left=left,
        text_right=right,
        text_top=y_text,
        text_bottom=text_bottom,
        cta_cy=cta_cy,
        cta_text=cta_txt,
        cta_font_px=cta_px,
        logo_box=(
            logo_x,
            y_logo_top,
            logo_x + logo_img.width,
            y_logo_top + logo_img.height,
        ),
    )
    finalize(canvas, out)


def main() -> int:
    global LAYOUT_DEBUG
    ap = argparse.ArgumentParser(
        description="Carrusel Instagram 1080×1350 — planes ParaguAI (Pillow)."
    )
    ap.add_argument(
        "--layout-debug",
        action="store_true",
        help="Superpone contornos de zona de copy, CTA y logo (revisión de layout).",
    )
    args = ap.parse_args()
    LAYOUT_DEBUG = args.layout_debug

    root = repo_root()
    logo_path = root / "brand" / "paraguai-logo.png"
    out_dir = root / "assets" / "creativos"
    if not logo_path.is_file():
        print(f"ERROR: falta logo en {logo_path}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    side_image_dir().mkdir(parents=True, exist_ok=True)

    builders = [
        ("paraguai-carousel-planes-01.png", build_slide1),
        ("paraguai-carousel-planes-02.png", build_slide2),
        ("paraguai-carousel-planes-03.png", build_slide3),
        ("paraguai-carousel-planes-04.png", build_slide4),
        ("paraguai-carousel-planes-05.png", build_slide5),
    ]
    for name, fn in builders:
        out = out_dir / name
        if args.layout_debug:
            stem = Path(name).stem
            out = out_dir / f"{stem}-layout-debug.png"
        fn(out, logo_path)
        print(f"OK {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
