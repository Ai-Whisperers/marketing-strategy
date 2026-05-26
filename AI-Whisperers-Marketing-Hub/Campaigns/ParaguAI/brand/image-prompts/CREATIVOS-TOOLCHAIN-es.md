# Herramientas para generación de creativos — ParaguAI

Objetivo: **publicaciones listas para Instagram** según [INSTAGRAM-STANDARDS-es.md](../INSTAGRAM-STANDARDS-es.md) (incl. **§1.1 layout**: **4:5** para carrusel de planes y promos nuevas; **1:1** para verticales `social-1080` hasta migración por brief) con marca consistente.

---

## Niveles (elegí según calidad vs. velocidad)

| Nivel | Herramienta | Cuándo usarla |
|-------|-------------|----------------|
| **A — Rápido y versionable** | `python scripts/build_carousel_planes_png.py` (Pillow) | Carrusel planes, placeholders, A/B de copy; todo en git sin API keys. |
| **B — IA raster** | Cursor **Generate Image** / Midjourney / etc. | Cuando necesités foto ilustración, escena 3D, textura; siempre con [image-prompt-es.md](../verticals/gymfit-py/image-prompt-es.md) aprobado y `paraguai-logo.png` **compositado después**. |
| **C — Producción** | Figma / Canva / Photoshop | Piezas finales para ads, pixel-perfect, animaciones export. |
| **D — Captura producto** | Playwright / Chromium (opcional) | Screenshot de demos en `paragu-ai.com` para Reels o “antes/después” (no reemplaza diseño de post). |

---

## Mejoras aplicadas al pipeline “A” (Pillow)

- **Sombra de tarjeta** con `GaussianBlur` (profundidad real, no rectángulo gris plano).
- **UnsharpMask** leve al exportar (texto más nítido en pantallas Retina).
- **Texto con contorno** sutil en títulos grandes (legibilidad sobre fondos con color).
- **Cadena de fuentes:** `PARAGUAI_FONT_DIR` → `brand/fonts/*.ttf` → Windows (`segoeuib`, `arialbd`, …).

Dependencias: ver [scripts/requirements-creativos.txt](../../scripts/requirements-creativos.txt).

---

## Checklist antes de publicar (cualquier nivel)

1. Nombre **ParaguAI** y URL **paragu-ai.com** correctos ([PARAGUAI-BRAND-GUIDE.md](../PARAGUAI-BRAND-GUIDE.md)).
2. Logo oficial visible donde corresponda (`brand/paraguai-logo.png`).
3. Copy sin “Google”; usar online / página web / internet (regla Cursor `paraguai-copy-language-rule.mdc` en el workspace).
4. Precios y claims alineados al sitio vivo.
5. PNG final en **`assets/creativos/`** con nombre estable ([creativos/README.md](../../assets/creativos/README.md)).

---

## Extender el repo (opcional, sin commitear secretos)

- **API de imagen** (Replicate, fal, OpenAI Images): usar variables de entorno locales y un script aparte; no guardar keys en el repo.
- **Plantilla Figma**: exportar PNG 1:1 y sólo versionar el enlace Figma en este doc o en Notion interno.
