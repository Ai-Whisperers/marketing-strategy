# ParaguAI — Guía de marca (obligatoria)

**Fuente oficial:** https://paragu-ai.com/  
**Assets locales:** esta carpeta (`brand/`)  
**Palabras y colores por rubro:** [WORDS-AND-COLORS-RESEARCH-es.md](WORDS-AND-COLORS-RESEARCH-es.md)  
**Copy sin “Google”:** regla `.cursor/rules/campaigns/paraguai-copy-language-rule.mdc` — usar **online**, **página web**, **internet**  
**Instagram (posts):** [INSTAGRAM-STANDARDS-es.md](INSTAGRAM-STANDARDS-es.md) · **Pipeline:** [OPERATIONS-PIPELINE-es.md](OPERATIONS-PIPELINE-es.md) · **Demos:** [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md)

---

## Nombre (exacto)

| Correcto | Incorrecto |
|----------|------------|
| **ParaguAI** | Paragu AI, Paraguay AI, PARAGU AI |
| **ParaguAI Builder** (titular producto / OG) | ParaguAI Builders, Paragu AI Builder |
| **paragu-ai.com** (URL, minúsculas) | paraguai.com, www.paragu-ai |

En imágenes y copy: la palabra **AI** del wordmark va en **mayúsculas** y color lavanda (no reescribir como "Ai" o "ai" dentro del logo).

---

## Logo oficial

| Archivo | Uso |
|---------|-----|
| [paraguai-logo.png](paraguai-logo.png) | Logo completo (ícono + wordmark) — **referencia obligatoria** para IA |
| [paraguai-og-reference.png](paraguai-og-reference.png) | Composición social / banner oscuro |

### Ícono (cuadrado)

- Cuadrado con división **diagonal** (esquina sup. izq. → inf. der.).
- **Triángulo superior izquierdo:** gradiente **púrpura → magenta/rosa**.
- **Triángulo inferior derecho:** **azul marino** casi negro.
- Texto **"AI"** centrado en **blanco**, sans-serif bold.

### Wordmark (pastilla)

- Fondo: **pastilla azul marino** redondeada.
- **"Paragu"** en **blanco**.
- **"AI"** en **lavanda / púrpura claro** (#B8A0FF aprox.).

**Prohibido en creativos:** inventar otro símbolo, cambiar colores del ícono, poner solo "Paragu" sin AI, usar tipografía script/handwritten para el logo.

---

## Paleta

| Token | Hex (aprox.) | Uso |
|-------|--------------|-----|
| Navy fondo | `#0F1419` – `#1A1F2C` | Fondos principales, pastilla logo |
| Blanco | `#FFFFFF` | Títulos, "Paragu" |
| Lavanda AI | `#B8A0FF` | "AI" en wordmark, acentos |
| Gradiente ícono | `#7C3AED` → `#EC4899` | Solo en el cuadrado del logo |
| Gris copy secundario | `#94A3B8` | Subtítulos en banners |
| Acento rubro | Variable | Solo en **contenido** del post (ej. verde gym), nunca reemplazar colores del logo |

---

## Tipografía (creativos)

**Norma completa (título, subtítulo, cuerpo, precios, espaciado):** [TYPOGRAPHY-POST-STANDARD-es.md](TYPOGRAPHY-POST-STANDARD-es.md).

- Familia principal: **Inter**; alternativas alineadas al estándar: **Plus Jakarta Sans**, **Montserrat**, **DM Sans** — instalación en [fonts/README.md](fonts/README.md).
- Títulos: bold / extra-bold. Subtítulos: medium / semibold. Cuerpo: regular.
- No usar serif decorativa en el lockup del logo ni como familia dominante en posts de producto salvo brief excepcional.

---

## Prompt antes de generar imágenes (obligatorio)

No generes PNG de campaña sin documento revisado:

1. Leé [brand/image-prompts/README.md](image-prompts/README.md) y [brand/image-prompts/WORKFLOW-pre-imagen-es.md](image-prompts/WORKFLOW-pre-imagen-es.md).
2. Por vertical: editá y aprobá `verticals/{slug}/image-prompt-es.md` (checklist pre-generación).
3. Recién después exportá el PNG en **`assets/creativos/vertical-<slug>-social-1080.png`** (ver [assets/creativos/README.md](../assets/creativos/README.md)).

---

## Composición en imágenes sociales (1080×1350 feed / 1080×1080 legacy)

Normas de layout detalladas (feed / carrusel, márgenes, ratios, jerarquía): [INSTAGRAM-STANDARDS-es.md](INSTAGRAM-STANDARDS-es.md) §1.1 y regla Cursor `paraguai-instagram-promotional-layout`.

1. **Logo:** esquina superior izquierda o inferior centrado — usar asset oficial o recomponer **pixel-fiel** al PNG de referencia.
2. **URL:** `paragu-ai.com` en gris claro, pie de imagen (como OG oficial).
3. **Titular producto** (opcional): "ParaguAI Builder" solo en piezas corporativas; en rubro usar "ParaguAI" + nombre del vertical (ej. GymFit).
4. **Espacio seguro:** margen mínimo 48px alrededor del logo.
5. **Fondo:** preferir navy oscuro o blanco limpio; evitar fondos que compitan con el gradiente del ícono.

---

## Prompt estándar (pegar en generación de imágenes)

```text
Use EXACTLY the ParaguAI brand from reference image paraguai-logo.png:
- Wordmark "ParaguAI" with "Paragu" white and "AI" light lavender on dark navy pill
- Square icon: diagonal purple-to-pink gradient top-left, dark navy bottom-right, white "AI"
- Do NOT alter spelling, colors, or invent a new logo
- Include paragu-ai.com in footer
Reference: AI-Whisperers-Marketing-Hub/Campaigns/ParaguAI/brand/paraguai-logo.png
```

---

## Descarga de assets actualizados

```powershell
# Desde la raíz del repo Marketing
Invoke-WebRequest -Uri "https://paragu-ai.com/logo.png" -OutFile "AI-Whisperers-Marketing-Hub/Campaigns/ParaguAI/brand/paraguai-logo.png"
Invoke-WebRequest -Uri "https://paragu-ai.com/og-default.png" -OutFile "AI-Whisperers-Marketing-Hub/Campaigns/ParaguAI/brand/paraguai-og-reference.png"
```

Revisar si el sitio actualiza el logo antes de campañas grandes.
