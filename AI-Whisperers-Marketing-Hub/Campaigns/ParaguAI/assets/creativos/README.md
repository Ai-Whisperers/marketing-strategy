# Creativos sociales (carpeta única)

Todos los **PNG de campaña** generados o exportados viven acá, con nombre estable, para que el pipeline y el diseño tengan **un solo lugar** donde buscar y versionar.

**No mover acá:** `brand/paraguai-logo.png` ni `brand/paraguai-og-reference.png` (son **fuente de marca**, no posts).

**Apoyo visual reutilizable (sin logo, para componer):** carpeta [elementos-apoyo/](elementos-apoyo/README.md) — ilustraciones laptop, teléfono, gym, belleza, comida, barbería, reservas, emprendedor.

---

## Índice de archivos

| Archivo | Uso |
|---------|-----|
| [elementos-apoyo/README.md](elementos-apoyo/README.md) | B-roll 1:1 (laptop, phone, rubros) — composición en posts |
| [paraguai-carousel-planes-01.png](paraguai-carousel-planes-01.png) | Carrusel planes — slide 1 hook |
| [paraguai-carousel-planes-02.png](paraguai-carousel-planes-02.png) | Carrusel planes — slide 2 Starter |
| [paraguai-carousel-planes-03.png](paraguai-carousel-planes-03.png) | Carrusel planes — slide 3 Profesional |
| [paraguai-carousel-planes-04.png](paraguai-carousel-planes-04.png) | Carrusel planes — slide 4 Negocio |
| [paraguai-carousel-planes-05.png](paraguai-carousel-planes-05.png) | Carrusel planes — slide 5 CTA + logo |
| [vertical-gymfit-py-social-1080.png](vertical-gymfit-py-social-1080.png) | Demo gym |
| [vertical-de-abasto-a-casa-social-1080.png](vertical-de-abasto-a-casa-social-1080.png) | Meal prep / ecommerce comida |
| [vertical-salon-maria-social-1080.png](vertical-salon-maria-social-1080.png) | Peluquería |
| [vertical-studio-belleza-social-1080.png](vertical-studio-belleza-social-1080.png) | Salón belleza |
| [paraguai-corporativo-48h-2026-05-20.png](paraguai-corporativo-48h-2026-05-20.png) | Pieza corporativa semana |
| [social-web-llamativo-2026-05.png](social-web-llamativo-2026-05.png) | Post web (v1) |
| [social-web-llamativo-2026-05-v2.png](social-web-llamativo-2026-05-v2.png) | Post web (v2, tono positivo) |
| [vetepy-social-2026-05-20.png](vetepy-social-2026-05-20.png) | Campaña VetePy (no paragu-ai.com) |

**Carrusel / piezas generales** (nombres legacy en `04-instagram-linkedin-posts-es.md`; agregar fila al exportar): `paraguai-social-hero-48h.png`, `paraguai-social-3-pasos.png`, `paraguai-social-starter-gratis.png`, `paraguai-social-proof-250.png`.

**Nuevos verticales:** al exportar, usar el patrón `vertical-<slug>-social-1080.png` (mismo `<slug>` que la carpeta en `verticals/`).

---

## Convención

- **1080×1080** salvo que el brief indique otro ratio.
- **Carrusel planes** (`paraguai-carousel-planes-0*.png`): **1080×1350** (4:5); columna visual opcional en [carousel-planes/](carousel-planes/README.md); regenerar con `python scripts/build_carousel_planes_png.py` (ver [10-carousel-planes-paraguai-es.md](../10-carousel-planes-paraguai-es.md) y [CREATIVOS-TOOLCHAIN-es.md](../../brand/image-prompts/CREATIVOS-TOOLCHAIN-es.md)).
- Después de generar: **compositá** el logo oficial desde `../brand/paraguai-logo.png` si hace falta.
