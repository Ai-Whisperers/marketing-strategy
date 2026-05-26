# Imágenes opcionales — carrusel planes (fondo del anuncio)

Si existen estos archivos, el script `scripts/build_carousel_planes_png.py` los usa como **fondo a pantalla completa** dentro de la tarjeta redondeada (plantilla tipo anuncio): se recortan al tamaño interior de la tarjeta, con un velo oscuro para que el copy centrado se lea bien. Si no hay archivo, se usa una **ilustración procedural** en el mismo formato.

| Archivo | Slide |
|---------|--------|
| `side-01.png` | Hook |
| `side-02.png` | Starter |
| `side-03.png` | Profesional |
| `side-04.png` | Negocio |
| `side-05.png` | Cierre / plan a medida |

**Lienzo del post:** **1080×1350 px** (4:5). El fondo ocupa el **rectángulo interior** de la tarjeta (márgenes `CARD_PAD` + `CARD_TOP_INSET` respecto al lienzo).

**Tamaño recomendado del asset:** **≥ 1000 px de alto** y **≥ 900 px de ancho** (o ratio similar 4:5); el script hace *fit* al rectángulo interior. Preferí imágenes **sin texto** para no competir con el titular.

**Formato:** PNG o JPG (se convierte a RGBA al cargar).

**Columnas actuales (`side-0*.png`):** generadas como apoyo visual IA (sin logo ni texto); revisá antes de publicar campaña oficial ([WORKFLOW-pre-imagen-es.md](../../brand/image-prompts/WORKFLOW-pre-imagen-es.md)).

Si no hay archivo, se usa una **ilustración procedural** (mockup simple) para no dejar la columna vacía.
