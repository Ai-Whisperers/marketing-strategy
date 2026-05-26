# Estándar tipográfico — posts ParaguAI (feed / carrusel)

**Audiencia:** diseño, prompts de imagen y scripts raster (Pillow).  
**Relacionado:** [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md) (paleta y logo) · [INSTAGRAM-STANDARDS-es.md](INSTAGRAM-STANDARDS-es.md) §1.1 · carrusel [10-carousel-planes-paraguai-es.md](../10-carousel-planes-paraguai-es.md) · script `scripts/build_carousel_planes_png.py` (`TextRow.role`).

---

## 1. Qué usan los anuncios digitales (patrones consolidados)

En display social y banners (Meta, Google, creatividades DTC / B2B SaaS) se repiten **cuatro ideas**, independientemente de la familia concreta:

| Patrón | Por qué funciona |
|--------|------------------|
| **Sans geométrica o neo-grotesk** | Legible en thumb, neutral, no compite con el producto ni el logo. |
| **Pocos niveles (2–3)** | Titular + apoyo + (opcional) legal/URL; más niveles = ruido y baja retención. |
| **Contraste de peso, no de familia** | Misma familia en Bold / Medium / Regular evita “mezcla de fonts” amateur. |
| **Titular corto, cuerpo más pequeño y más aire** | El ojo escanea en **F** o **Z**; el espacio entre titular y subtítulo refuerza jerarquía igual que el tamaño. |

**Familias que verás una y otra vez** (por sector, no como obligación de copia):

- **Producto tech / SaaS:** Inter, SF Pro, IBM Plex Sans, sistemas “UI” legibles a tamaño pequeño.  
- **Marca global genérica:** Helvetica / Arial / sistemas del SO (rápidos de producir).  
- **Retail / promos con “voz”:** Montserrat, Poppins, Oswald en titulares; cuerpo regular de la misma familia.  
- **Startups “friendly”:** Plus Jakarta Sans, DM Sans, circular/geometric rounds.

**ParaguAI** encaja en **tech + local B2B**: sans moderna, 2–3 pesos, fondo oscuro y acentos de marca ya definidos en la guía.

---

## 2. Principios del estándar (norma de diseño)

1. **Una familia principal por pieza** (carrusel completo o post único). Variantes **Bold / SemiBold / Medium / Regular** de esa familia, no mezclar dos sans distintas salvo excepción acordada (p. ej. solo logo vs copy).  
2. **Titular:** máximo contraste (blanco o lavanda de marca), peso **Bold** o **ExtraBold** si existe; en fotos ruidosas, **contorno sutil** o scrim (ya contemplado en plantillas tipo anuncio).  
3. **Subtítulo / línea de apoyo:** **Medium o SemiBold** — distinto del titular por **peso + tamaño + aire**, no solo por color.  
4. **Cuerpo y viñetas:** **Regular** (o Medium muy moderado en labels “Qué incluye”). Tamaño mínimo coherente con [INSTAGRAM-STANDARDS-es.md](INSTAGRAM-STANDARDS-es.md) (~18–20 px efectivos en 1080 px de ancho para cuerpo).  
5. **Precios / CTA en imagen:** Bold o SemiBold, tamaño intermedio entre titular y cuerpo; no más de **una** frase CTA dominante por slide.  
6. **No:** serif decorativa, script, “display” fantasía en copy de producto (salvo campaña explícita fuera de esta norma). El logo mantiene su propia regla en [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md).

---

## 3. Stack tipográfico oficial ParaguAI (orden de preferencia)

Instalación recomendada: archivos `.ttf` / `.otf` estáticos en **`brand/fonts/`** — pasos y enlaces de descarga en [fonts/README.md](fonts/README.md). Alternativa: variable de entorno `PARAGUAI_FONT_DIR` para CI.

| Prioridad | Familia | Uso en posts |
|-----------|---------|----------------|
| 1 | **Inter** | Principal: UI-like, excelente en tamaños pequeños y medianos. |
| 2 | **Plus Jakarta Sans** | Alternativa con un poco más de carácter; mismos roles (Bold / Medium / Regular). |
| 3 | **Montserrat** | Titulares muy “poster”; cuerpo legible si no hay Inter. |
| 4 | **DM Sans** | Alternativa “friendly”; mismo esquema de pesos. |
| Fallback | **Segoe UI** / **Arial** (sistema) | Solo si no hay ningún `.ttf` de marca en `brand/fonts/`. |

Los scripts de carrusel resuelven la fuente en ese orden lógico (ver `pick_font`, `pick_font_subtitle` en `build_carousel_planes_png.py`).

---

## 4. Roles de texto → peso, color y tamaño (referencia 1080 px ancho)

Valores en **px** son **orientativos** para plantillas raster; ajustar con `fit_and_draw_text_column` o equivalente si el copy es más largo.

| Rol | Contenido típico | Peso | Color (tokens marca) | Tamaño ref. (ancho 1080) | Notas |
|-----|------------------|------|------------------------|---------------------------|--------|
| **Título / headline** | Hook, nombre del plan, promesa corta | **Bold** | `WHITE` o `LAVENDER` | **40–52 px** (4:5 puede subir 2–4 px si hay poco copy) | Contorno opcional solo en titulares grandes sobre foto; `role="headline"` en script. |
| **Subtítulo** | Línea de apoyo bajo el titular (“Sitio profesional en 48 h”) | **Medium o SemiBold** | `MUTED` o lavanda suave | **~0,55–0,65×** el headline (ej. 24–30 px) | **+ aire** respecto al titular (`HEADLINE_TO_SUBTITLE_EXTRA_GAP` en script); `role="subtitle"`. |
| **Etiqueta / sección** | “Qué incluye”, “Qué suma…” | **SemiBold / Medium** | `LAVENDER_MUTED` o similar | **~18–22 px** | `role="label"`. |
| **Cuerpo / bullets** | Listas, detalle | **Regular** (bold solo énfasis puntual) | `MUTED` | **18–22 px** | Máx. 2–4 líneas de apoyo por slide en promos; `role="body"`. |
| **Precio / dato** | “Setup: Gs. …”, “+ Gs. …/mes” | **Bold** | `LAVENDER` / `WHITE` | **28–34 px** | Separar visualmente del cuerpo; `role="price"` o `headline` sin contorno según diseño. |
| **Pie / URL** | `paragu-ai.com` | **Regular o Medium** | gris claro guía | **22–28 px** | No competir con el titular; reglas en guía de marca. |

**Relación titular : cuerpo:** mantener aprox. **2,3×–3×** en tamaño (alineado a §1.1 Instagram estándares).

---

## 5. Espaciado vertical (ritmo)

| Entre | Recomendación |
|-------|----------------|
| Líneas del mismo bloque | Gap mínimo constante (p. ej. 12 px) + extra opcional tras líneas muy altas. |
| **Última línea del titular → primera del subtítulo** | **+24–32 px** adicionales al gap normal (constante `HEADLINE_TO_SUBTITLE_EXTRA_GAP` en el script de carrusel). |
| Bloque de copy → CTA en pie | Reservar franja (p. ej. `GAP_TEXT_TO_CTA` en script) para que IG no tape el mensaje. |

---

## 6. Mapeo técnico (carrusel planes y futuros scripts)

En `TextRow` del generador PNG:

| `role` | Comportamiento tipográfico |
|--------|----------------------------|
| `headline` | `pick_font(..., bold=True)`; contorno si `outline=True` y tamaño grande. |
| `subtitle` | Stack **Medium → SemiBold → Regular** (`pick_font_subtitle`). |
| `label` | Igual que subtitle (peso intermedio). |
| `body` | Regular / bold según flag `bold` del row. |
| `price` | Siempre bold para números y cifras. |

Añadir **`gap_before`** en px cuando un bloque necesite más separación explícita (p. ej. después de un mockup).

---

## 7. Checklist antes de publicar

- [ ] Misma **familia** (o stack oficial de fallback) en todas las slides del carrusel.  
- [ ] Solo **2–3 niveles** de tamaño/peso perceptibles.  
- [ ] Subtítulo **separado** del titular (aire + peso Medium, no otro Bold igual al headline).  
- [ ] Cuerpo **≥ ~18 px** en 1080 de ancho; revisar thumb.  
- [ ] Contraste suficiente sobre fondo (ver guía de marca).  
- [ ] Logo y URL no usan una tercera familia distinta del copy (el logo es asset, no “font” libre).

---

## 8. Cambios futuros

- Si el sitio **paragu-ai.com** adopta una fuente web distinta, actualizar esta tabla y los nombres de archivo esperados en `brand/fonts/`.  
- Para **Reels / Stories 9:16**, reescalar proporcionalmente; mantener los mismos **roles** y ratios.
