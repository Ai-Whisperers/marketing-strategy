# Estándares Instagram — ParaguAI

Documento normativo para **copy**, **creativos** y **publicación** alineados a [paragu-ai.com](https://paragu-ai.com/). Mercado: **Paraguay**. Idioma: **español paraguayo** (vos, tono directo, sin paternalismo).

**Relacionado:** [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md) · [TYPOGRAPHY-POST-STANDARD-es.md](TYPOGRAPHY-POST-STANDARD-es.md) · [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md) · reglas `.cursor/rules/campaigns/paraguai-*` (incl. **layout promocional** `paraguai-instagram-promotional-layout`)

---

## Formatos y dimensiones

| Formato | Ratio | Tamaño recomendado | Uso |
|---------|-------|-------------------|-----|
| Feed / carrusel (promos, **carrusel planes** ParaguAI) | **4:5** | **1080×1350 px** | Mayor superficie en móvil; **todas** las slides del mismo post con el **mismo ratio**. |
| Post cuadrado (legacy / verticales `social-1080`) | 1:1 | 1080×1080 px | Demos por rubro hasta que el brief pase a 4:5. |
| Post horizontal | 1.91:1 | 1080×566 px | Solo si el creativo es nativamente horizontal. |
| Reels | 9:16 | 1080×1920 px | Hook 0–3 s; zona segura: no texto crítico en los ~250 px inferiores (UI de IG). |
| Stories | 9:16 | 1080×1920 px | Sticker enlace arriba; CTA legible en tercio medio. |

**Creativos por rubro (export estándar hoy):** `assets/creativos/vertical-<slug>-social-1080.png` (**1:1**) — ver [assets/creativos/README.md](../assets/creativos/README.md). **Carrusel de planes:** `paraguai-carousel-planes-0*.png` en **1080×1350** (ver [10-carousel-planes-paraguai-es.md](../10-carousel-planes-paraguai-es.md)). Otras **piezas nuevas** en feed pueden planificarse en **4:5** aunque el vertical siga en 1:1.

### 1.1 Layout promocional (feed y carrusel) — estándar 2025-2026

Referencia de producto y prácticas públicas consolidadas (Meta / creadores / guías de tamaño 2025-2026): carruseles con **ratio uniforme**, **primera slide = gancho**, **última slide = CTA + marca**; formato **4:5** recomendado para nuevas campañas por mayor tiempo en pantalla vs 1:1.

**Regla Cursor (agente):** `.cursor/rules/campaigns/paraguai-instagram-promotional-layout-rule.mdc`.

| Tema | Estándar |
|------|-----------|
| **Una idea por slide** | Un titular dominante + apoyo breve (y opcional viñetas o imagen). Evitar muros de texto. |
| **Titular en slide** | Ideal **≤ 8 palabras**; si el mensaje es largo, partilo en dos líneas con contraste distinto, no en un solo bloque denso. |
| **Cuerpo / bullets** | Máximo **~2–4 líneas** de apoyo por slide en promos; listas con **•** o **–**, líneas cortas. |
| **Jerarquía visual** | 1) Titular (máximo tamaño y contraste) → 2) Visual (foto, mockup, ilustración, columna derecha) → 3) Copy secundario → 4) Marca (logo + URL) en pie o slide de cierre. |
| **Tipografía mínima** | Sobre **1080 px** de ancho: cuerpo **≥ ~18–20 px** efectivos; titular **~2.3×–3×** el cuerpo. En **4:5** (1350 alto), escalá proporcionalmente si el diseño lo amerita. Roles (headline / subtitle / body) y stack de fuentes: [TYPOGRAPHY-POST-STANDARD-es.md](TYPOGRAPHY-POST-STANDARD-es.md). |
| **Márgenes** | **≥ 48 px** a bordes para logo y elementos críticos (coherente con composición en `PARAGUAI-BRAND-GUIDE.md`). Dejá **espacio reservado** entre bloque de copy y CTA para compresión de Instagram y thumbs. |
| **Zona “grid” del perfil** | Si usás **4:5**, la miniatura del perfil puede recortar; mantené **foco y titular** dentro del **tercio central** vertical cuando importe el preview en grilla **3:4**. |
| **Carrusel planes ParaguAI** | Storyboard y precios: [10-carousel-planes-paraguai-es.md](../10-carousel-planes-paraguai-es.md). Raster **1080×1350**: `scripts/build_carousel_planes_png.py` + opcionales `assets/creativos/carousel-planes/side-NN.png`. |
| **Patrón tipo B2B / IA (referencia industria)** | Fondo oscuro legible, titular grande, **columna visual** o mockup, CTA claro en última slide — coherente con carruseles educativos de producto (p. ej. marcas de IA / SaaS con slides “tipografía + diagrama”). No copiar terceros: adaptar a **marca ParaguAI** (guía + logo). |

**Checklist rápido (diseño):**

- [ ] Todas las slides del mismo carrusel: **mismo ratio y misma familia tipográfica**.
- [ ] Slide 1: **hook** sin depender del caption.
- [ ] Slides intermedias: **un solo mensaje** cada una.
- [ ] Última slide: **un CTA** + logo + `paragu-ai.com` (o acción acordada).
- [ ] Nada crítico en el **borde inferior extremo** si el CTA es solo texto pequeño.
- [ ] Revisión en **tamaño thumb** (¿se lee el titular?).

---

## 2. Marca en todo creativo

1. **Logo oficial** visible (esquina según [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md)).
2. **Nombre:** ParaguAI (exacto). URL en pie: `paragu-ai.com` (minúsculas, guion).
3. **No** sustituir colores del logo por el color “del rubro” encima del lockup.
4. Contraste WCAG: texto principal sobre fondo ≥ 4.5:1 cuando sea posible.

---

## 3. Estructura del caption (feed)

Orden fijo para consistencia y para que el pipeline genere siempre el mismo esqueleto:

1. **Hook** (1 línea, ≤ 12 palabras) — dolor, pregunta o dato.
2. **Cuerpo** (2–5 líneas cortas) — un solo mensaje; beneficios concretos (48h, .com.py, demo gratis).
3. **Prueba o credencial** (1 línea opcional) — cifras oficiales del sitio si aplican.
4. **CTA** — “Demo gratis” + WhatsApp o “Link en bio” con acción clara.
5. **Hashtags** — 5 a 10; mezcla 2–3 amplios (#Paraguay #EmprendedoresPY) + nicho (#PeluqueriaPy). Sin bloques de 30 hashtags.

**Longitud:** apuntar a **≤ 2.200 caracteres** total (caption + hashtags); si el carrusel cuenta la historia, el caption puede ser más corto.

---

## 4. Tonos prohibidos y reemplazos

| Evitar | Preferir |
|--------|----------|
| “Google”, “googlear” | online, internet, página web, buscador (neutro) |
| Promesas no publicadas en la web | Solo lo verificable en paragu-ai.com |
| Inglés innecesario en hook | Español; anglicismos solo si son comunes en PY |
| Humo / “revolucionario” | Directo, confiable, local |

---

## 5. Deep link por pieza

Cada post que muestra un **ejemplo de rubro** debe llevar UTM coherente y URL de demo correcta:

- Patrón: `https://paragu-ai.com/{path}?utm_source=instagram&utm_medium=organic&utm_campaign={slug_vertical}`
- Lista canónica de paths: [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md).

**Bio:** un solo link principal; campañas pueden usar `utm_campaign` distinto por mes.

---

## 6. Carrusel (estructura promocional)

Alineado a **§1.1 Layout promocional** y a la regla `.cursor/rules/campaigns/paraguai-instagram-promotional-layout-rule.mdc`.

| Slide típico | Contenido | Texto en imagen (guía) |
|--------------|------------|-------------------------|
| 1 | Hook + promesa o dolor | Titular corto; tipografía grande |
| 2 … N−1 | Valor (beneficio, plan, paso, prueba) | Una idea; bullets breves si aplica |
| N | CTA + marca | Logo + URL + una acción |

**Carrusel de planes (repo):** ver [10-carousel-planes-paraguai-es.md](../10-carousel-planes-paraguai-es.md) — nombres de planes alineados a [paragu-ai.com](https://paragu-ai.com/).

**Caption del carrusel:** la primera línea debe poder leerse sola como resumen del hook; no repitas todo el texto de cada slide.

## 7. Reels (25–30 s)

- **0–3 s:** pregunta o afirmación fuerte (sin logo tapando rostro si hay UGC).
- **4–12 s:** problema (solo IG no alcanza, horarios, profesionalismo).
- **13–22 s:** solución ParaguAI + demo en pantalla (scroll del sitio real del vertical).
- **23–30 s:** CTA verbal + texto en pantalla “Demo gratis · link en bio”.
- Subtítulos **quemados** o caption detallado (accesibilidad).

---

## 8. Stories

- Máx. **1 idea por story**; si hay encuesta, 2 opciones claras.
- Sticker enlace a la **misma URL** que el feed si la campaña es la misma semana.
- Tipografía mínima equivalente a ~24 px en 1080 de ancho para legibilidad en móvil.

---

## 9. Checklist pre-publicación (Instagram)

- [ ] URL de demo coincide con [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md) para ese rubro.
- [ ] UTM presente en enlaces trackeables (bio o comentario fijado si aplica API).
- [ ] Logo y nombre ParaguAI correctos en imagen/video.
- [ ] Copy revisado con regla sin “Google”.
- [ ] CTA único (no mezclar “llamar” + “DM” + “link” en igual peso).
- [ ] Texto alternativo / descripción para accesibilidad (guardar en metadatos del pipeline o primer comentario).

---

## 10. Métricas mínimas por pieza

Registrar por slot (aunque sea export CSV):

| Campo | Ejemplo |
|-------|---------|
| `fecha` | 2026-05-26 |
| `formato` | carousel / reel / story |
| `vertical_slug` | salon-maria |
| `url_demo` | https://paragu-ai.com/salon-maria?... |
| `alcance` | (del panel) |
| `guardados` | |
| `clics_bio` | si hay Bitly/UTM |

Revisión semanal: top 2 piezas por **guardados + completación de reel**; replicar hook, no solo diseño.
