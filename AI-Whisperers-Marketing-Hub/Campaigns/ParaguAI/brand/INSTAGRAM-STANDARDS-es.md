# Estándares Instagram — ParaguAI

Documento normativo para **copy**, **creativos** y **publicación** alineados a [paragu-ai.com](https://paragu-ai.com/). Mercado: **Paraguay**. Idioma: **español paraguayo** (vos, tono directo, sin paternalismo).

**Relacionado:** [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md) · [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md) · reglas `.cursor/rules/campaigns/paraguai-*`

---

## 1. Formatos y dimensiones

| Formato | Ratio | Tamaño recomendado | Uso |
|---------|-------|-------------------|-----|
| Post cuadrado | 1:1 | 1080×1080 px | Feed principal, carrusel (cada slide 1080×1080) |
| Post vertical feed | 4:5 | 1080×1350 px | Máx. real estate en feed (opcional) |
| Reels | 9:16 | 1080×1920 px | Hook 0–3 s; zona segura: no texto crítico en los 250 px inferiores (UI de IG) |
| Stories | 9:16 | 1080×1920 px | Sticker enlace arriba; CTA legible en tercio medio |

**Creativos por rubro:** export estándar en **`assets/creativos/vertical-<slug>-social-1080.png`** (1:1) — ver [assets/creativos/README.md](../assets/creativos/README.md).

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

## 6. Carrusel (5 slides típico)

| Slide | Contenido | Texto en imagen (máx.) |
|-------|------------|-------------------------|
| 1 | Hook + dolor | ≤ 8 palabras, tipografía grande |
| 2 | Solución ParaguAI | beneficio único |
| 3 | Prueba social / dato PY | 1 número o 1 frase |
| 4 | Proceso en 3 pasos | WhatsApp → armamos → publicamos |
| 5 | CTA + demo gratis | logo + URL |

**Caption del carrusel:** resume slide 1 en la primera línea; no repitas todo el texto de cada slide.

---

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
