# Documentación de prompts — imágenes ParaguAI

Antes de generar cualquier PNG en **`assets/creativos/`** (p. ej. `vertical-<slug>-social-1080.png`), el prompt debe existir en **Markdown**, revisarse y aprobarse. Así se corrige copy, claims y marca **antes** de gastar créditos de IA o tiempo en diseño.

## Orden de trabajo

1. **Brief** — Datos del rubro en `verticals/{slug}/README.md` (demo, colores, headline/sub propuestos).
2. **Prompt revisable** — Mismo slug: [`verticals/{slug}/image-prompt-es.md`](../verticals/gymfit-py/image-prompt-es.md) (un archivo por vertical). Editá la sección *Texto en imagen* y el bloque *Prompt listo para pegar* si hace falta.
3. **Checklist** — Completá *pre-generación* en ese `image-prompt-es.md`.
4. **Generación** — Recién ahí: herramienta de imagen con referencia `brand/paraguai-logo.png`.
5. **Salida** — Exportar como `assets/creativos/vertical-<slug>-social-1080.png` (1080×1080). Ver [creativos/README.md](../assets/creativos/README.md).

## Documentos de apoyo

| Documento | Uso |
|-----------|-----|
| [CREATIVOS-TOOLCHAIN-es.md](CREATIVOS-TOOLCHAIN-es.md) | **Stack de herramientas** (Pillow vs IA vs Figma), mejoras del pipeline y checklist |
| [WORKFLOW-pre-imagen-es.md](WORKFLOW-pre-imagen-es.md) | Resumen del flujo y responsabilidades |
| [../PARAGUAI-BRAND-GUIDE.md](../PARAGUAI-BRAND-GUIDE.md) | Logo, nombre, URL, tono |
| [paraguai-brand-visual-rule.mdc](../../../../../.cursor/rules/campaigns/paraguai-brand-visual-rule.mdc) | Estándar visual obligatorio |
| [paraguai-copy-language-rule.mdc](../../../../../.cursor/rules/campaigns/paraguai-copy-language-rule.mdc) | Lenguaje neutro (online, página web, internet) |

## Regenerar prompts desde README

Si actualizás muchos `README.md` y querés sincronizar el bloque “Brief desde README” y el prompt en cada `image-prompt-es.md`:

```powershell
python AI-Whisperers-Marketing-Hub/Campaigns/ParaguAI/scripts/gen-vertical-image-prompts.py
```

(Ejecutar desde la raíz del repo `AI-Whisperers-Marketing-Hub` o ajustar la ruta al script.)

## Creativos generales (no vertical)

Para piezas en `assets/` (hero, carrusel, prueba social), creá antes un archivo en esta carpeta, por ejemplo `PROMPT-{nombre}-es.md`, con la misma estructura de checklist que en `verticals/*/image-prompt-es.md`, y enlazalo desde el markdown del post correspondiente.
