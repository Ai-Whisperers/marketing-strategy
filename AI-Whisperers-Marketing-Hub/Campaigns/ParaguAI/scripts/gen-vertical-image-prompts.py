import re
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "verticals"


def parse_readme(text: str) -> dict:
    d: dict = {}
    m = re.search(r"\*\*Demo\*\*\s*\|\s*\[([^\]]+)\]\(([^)]+)\)", text)
    if m:
        d["demo_label"] = m.group(1)
        d["demo_url"] = m.group(2)
    m = re.search(r"\*\*Slogan rubro\*\*\s*\|\s*([^\n|]+)", text)
    d["slogan"] = m.group(1).strip() if m else ""
    m = re.search(r"\*\*Colores acento\*\*\s*\|\s*([^\n]+)", text)
    d["colores"] = m.group(1).strip() if m else ""
    m = re.search(r"\*\*Headline:\*\*\s*([^\n]+)", text)
    d["headline"] = m.group(1).strip() if m else ""
    m = re.search(r"\*\*Sub:\*\*\s*([^\n]+)", text)
    d["sub"] = m.group(1).strip() if m else ""
    m = re.search(r"^#\s+(.+)$", text, re.M)
    d["title"] = m.group(1).strip() if m else ""
    return d


CHECKLIST = """## Checklist pre-generación (corregir aquí antes de IA)

- [ ] Headline y sub cumplen [paraguai-copy-language-rule.mdc](../../../../../.cursor/rules/campaigns/paraguai-copy-language-rule.mdc) (online, página web, internet; sin marcas de buscadores ajenas).
- [ ] Nombre de marca **ParaguAI** (una palabra) y URL **paragu-ai.com** acordados con [PARAGUAI-BRAND-GUIDE.md](../../brand/PARAGUAI-BRAND-GUIDE.md).
- [ ] Colores de acento del rubro coherentes con [WORDS-AND-COLORS-RESEARCH-es.md](../../brand/WORDS-AND-COLORS-RESEARCH-es.md).
- [ ] Referencia de logo: `brand/paraguai-logo.png` adjunta al generador cuando el tool lo permita.

## Tras aprobar lo anterior

1. Generar imagen 1080×1080.
2. Verificar logo y footer con [paraguai-brand-visual-rule.mdc](../../../../../.cursor/rules/campaigns/paraguai-brand-visual-rule.mdc).
3. Guardar como **`social-1080.png`** en esta carpeta.
4. Actualizar [README.md](README.md) si cambió headline/sub.

## Checklist post-generación

- [ ] Logo ParaguAI coincide con referencia (o compositaste el PNG oficial).
- [ ] Texto en imagen coincide con la sección “Texto en imagen” de este archivo.
- [ ] No hay marcas de terceros prohibidas en copy visible.
"""


def main() -> None:
    for folder in sorted(base.iterdir()):
        if not folder.is_dir() or folder.name.startswith("_"):
            continue
        slug = folder.name
        readme = folder / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        d = parse_readme(text)
        title = d.get("title", slug)
        demo_url = d.get("demo_url", "")
        colores = d.get("colores", "(ver WORDS-AND-COLORS)")
        headline = d.get("headline", "")
        sub = d.get("sub", "")
        slogan = d.get("slogan", "")

        prompt_block = (
            "Creativo cuadrado 1080x1080 px para Instagram, mercado Paraguay, estilo moderno y limpio.\n\n"
            "Marca: ParaguAI (nombre exacto). Incluí el logo oficial de ParaguAI (referencia: archivo "
            "paraguai-logo.png) y en el pie el texto paragu-ai.com en tipografía legible.\n\n"
            f"Rubro / demo: {title} — URL demo: {demo_url}\n\n"
            f"Paleta: fondo sobrio; acentos del rubro: {colores}. No reinventes el logotipo ParaguAI: "
            "usá el lockup oficial o compositá el PNG de marca después.\n\n"
            "Texto principal en español (máx. 2 líneas cortas):\n"
            f"HEADLINE: {headline}\n"
            f"SUB: {sub}\n\n"
            f"Slogan de contexto (opcional, pequeño): {slogan}\n\n"
            "Texto visible: solo términos neutros para visibilidad (online, página web, internet). "
            "Ninguna marca de buscadores o mapas de terceros en el diseño.\n\n"
            "Composición: headline grande arriba o al centro, sub debajo, logo ParaguAI en esquina "
            "inferior o superior con buen margen, dominio paragu-ai.com al pie."
        )

        body = (
            f"# Prompt creativo — `{slug}` (revisar antes de generar)\n\n"
            "> **Flujo:** completá y corregí este documento → marcá el checklist pre-generación → "
            "recién ahí generá `social-1080.png`.\n\n"
            "## Especificaciones fijas\n\n"
            "| Campo | Valor |\n"
            "|-------|--------|\n"
            "| Salida | `social-1080.png` en esta carpeta (1080×1080 px) |\n"
            "| Logo | Referencia obligatoria: [brand/paraguai-logo.png](../../brand/paraguai-logo.png) |\n"
            "| Copy | [paraguai-copy-language-rule.mdc](../../../../../.cursor/rules/campaigns/paraguai-copy-language-rule.mdc) |\n"
            "| Visual | [paraguai-brand-visual-rule.mdc](../../../../../.cursor/rules/campaigns/paraguai-brand-visual-rule.mdc) |\n\n"
            "## Brief desde README\n\n"
            f"| Demo | {demo_url} |\n"
            f"| Slogan rubro | {slogan} |\n"
            f"| Colores acento | {colores} |\n\n"
            "## Texto en imagen (aprobar literal; editá acá si cambiás el creativo)\n\n"
            f"**Headline:** {headline}\n\n"
            f"**Sub:** {sub}\n\n"
            "## Prompt listo para pegar en IA (imagen)\n\n"
            "```text\n"
            f"{prompt_block}\n"
            "```\n\n"
            f"{CHECKLIST}"
        )
        (folder / "image-prompt-es.md").write_text(body, encoding="utf-8")
        print("wrote", folder / "image-prompt-es.md")


if __name__ == "__main__":
    main()
