# Flujo obligatorio: documento de prompt → imagen

## Objetivo

Evitar publicar creativos que incumplan marca ParaguAI (logo, nombre, URL) o [lenguaje de copy](../../../../../.cursor/rules/campaigns/paraguai-copy-language-rule.mdc).

## Reglas

1. **No generar** PNG en `assets/creativos/` sin un `.md` de prompt aprobado en el repo (o en la misma tarea con checklist marcado).
2. El documento de prompt es la **fuente de verdad** del texto que debe aparecer en la imagen; la IA o Figma deben alinear el render a ese texto.
3. Si el resultado visual “inventa” otro logotipo, **compositá** `brand/paraguai-logo.png` encima en lugar de aceptar el error.

## Por vertical

| Paso | Acción |
|------|--------|
| 1 | Abrí `verticals/{slug}/image-prompt-es.md`. |
| 2 | Revisá *Texto en imagen* y el bloque en ```text```. Corregí ortografía, tono y claims. |
| 3 | Marcá todos los ítems de *Checklist pre-generación*. |
| 4 | Generá la imagen (1080×1080) con referencia de logo. |
| 5 | Marcá *Checklist post-generación* y guardá el PNG en `assets/creativos/` con el nombre del vertical (ver README de creativos). |
| 6 | El caption en `posts-es.md` debe ser coherente con el creativo aprobado. |

## Piezas globales (`assets/`)

Misma lógica: creá `brand/image-prompts/PROMPT-<tema>-es.md` antes del PNG; en el markdown del post enlazá a ese prompt.

## Qué hacer si una imagen existente está mal

Borrá el PNG que no cumpla estándares, corregí el `image-prompt-es.md` (o el PROMPT global), volvé a generar y exportá de nuevo.
