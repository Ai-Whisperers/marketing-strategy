# Prompts para posts — ParaguAI

Antes de generar: [brand/INSTAGRAM-STANDARDS-es.md](brand/INSTAGRAM-STANDARDS-es.md) (formato + caption) · [brand/VERTICAL-DEMOS.md](brand/VERTICAL-DEMOS.md) (URLs) · [brand/OPERATIONS-PIPELINE-es.md](brand/OPERATIONS-PIPELINE-es.md) (etapas).

Estos prompts alimentan el **pipeline automático** (generación de copy → revisión mínima si aplica → upload). Calendario tipo: [02-marketing-plan-es.md](02-marketing-plan-es.md) § calendario rotativo.

Usá estos prompts en Cursor, Claude o ChatGPT para generar variantes. Siempre pedí **español paraguayo**, tono cercano, y CTA a demo gratis.

## Marca (obligatorio antes de generar imágenes)

1. Leer [brand/PARAGUAI-BRAND-GUIDE.md](brand/PARAGUAI-BRAND-GUIDE.md), [brand/WORDS-AND-COLORS-RESEARCH-es.md](brand/WORDS-AND-COLORS-RESEARCH-es.md) (rubro), [brand/INSTAGRAM-STANDARDS-es.md](brand/INSTAGRAM-STANDARDS-es.md) (formatos y caption)
2. Aplicar [paraguai-copy-language-rule.mdc](../../../.cursor/rules/campaigns/paraguai-copy-language-rule.mdc) — **no usar “Google”**; preferir **online**, **página web**, **internet**
3. Usar referencia `brand/paraguai-logo.png` en toda generación de imagen
4. Aplicar regla `.cursor/rules/campaigns/paraguai-brand-visual-rule.mdc`
5. Nombre exacto: **ParaguAI** (no Paragu AI). URL: **paragu-ai.com**
6. **Imagen por rubro:** no generar PNG sin documento — seguir [brand/image-prompts/README.md](brand/image-prompts/README.md); por vertical editar y aprobar `verticals/{slug}/image-prompt-es.md` antes de exportar a [assets/creativos/](assets/creativos/README.md) (`vertical-<slug>-social-1080.png`).

---

## Prompt maestro (cualquier red)

```text
Sos copywriter para ParaguAI (paragu-ai.com): sitios web profesionales para negocios paraguayos en 48 horas, todo incluido (diseño, dominio .com.py, SEO, WhatsApp). 

Audiencia: dueño de PYME en Paraguay, 30-55 años, usa WhatsApp todo el día, muchos solo tienen Instagram.

Objetivo del post: [DEMO GRATIS / PRUEBA SOCIAL / EDUCAR / RUBRO ESPECÍFICO]
Red: [Instagram carrusel / Reel guion / LinkedIn / Facebook]
Rubro (opcional): [peluquería / restaurante / gym / consultoría]

Escribí:
1) Hook (máx 12 palabras) que pare el scroll
2) Cuerpo (máx 120 palabras) con un solo mensaje claro
3) CTA con "Demo gratis" y WhatsApp
4) 5 hashtags mixtos (#Paraguay #EmprendedoresPY + 3 nicho)
5) Texto alternativo para imagen accesible

Datos que podés usar: 250+ sitios, 48h, 4.9 estrellas, 98% clientes felices, plan Starter gratis 3 meses, garantía 30 días, sin contrato.

NO uses inglés. NO prometas lo que no está en la web. Tono: confiable, directo, sin humo.
```

---

## Prompt — Carrusel Instagram (5 slides)

```text
Generá un carrusel de 5 slides para Instagram sobre ParaguAI.

Estructura obligatoria:
Slide 1: hook con dolor (perder clientes online / solo Instagram)
Slide 2: solución (sitio en 48h, todo incluido)
Slide 3: prueba social (250+ negocios PY o caso real)
Slide 4: proceso 3 pasos (WhatsApp → armamos → publicamos .com.py)
Slide 5: CTA demo gratis + garantía

Cada slide: máx 35 palabras, texto grande, emojis mínimos (0-2 por slide).
Incluí caption para IG (150 palabras) + pregunta final para comentarios.
```

---

## Prompt — Reel (guion 25 segundos)

```text
Escribí guion de Reel 25s para ParaguAI, formato hook-problema-solución-CTA.

Segundos 0-3: hook verbal fuerte ("¿Tu negocio tiene página web?")
Segundos 4-12: problema (Instagram no alcanza, mensajes a deshora)
Segundos 13-20: solución (48h, mandás datos por WhatsApp, dominio .com.py)
Segundos 21-25: CTA ("Link en bio — demo gratis")

Incluí: texto en pantalla por escena, sugerencia de B-roll (pantalla celular, Maps, WhatsApp).
```

---

## Prompt — LinkedIn (credibilidad B2B)

```text
Post LinkedIn para ParaguAI orientado a consultores, inmobiliarias o estudios profesionales en Paraguay.

Ángulo: tu portafolio en un dominio .com.py genera confianza antes de la primera reunión.
Longitud: 180-220 palabras.
Incluí: una estadística o insight sobre búsqueda online de servicios profesionales.
CTA suave: ver casos reales en paragu-ai.com o pedir demo.
Tono: profesional pero humano, sin corporativismo vacío.
```

---

## Prompt — Post por rubro (segmentado)

```text
Creá un post Instagram para dueños de [RUBRO] en Paraguay.

Usá el dato del mercado si aplica (ej. miles de peluquerías en PY en paragu-ai.com).
Mencioná beneficio específico del rubro:
- Peluquería: fotos de trabajos + WhatsApp + Maps
- Restaurante: menú + pedidos WhatsApp
- Gym: horarios y planes
- Consultoría: portafolio y contacto

Terminá con: "Tu rubro ya tiene diseño en ParaguAI. Demo gratis."
```

---

## Prompt — Imagen (DALL·E / Midjourney / Cursor)

```text
Imagen cuadrada 1080x1080 para redes sociales — ParaguAI (sitios web PY).

REFERENCE IMAGE (required): AI-Whisperers-Marketing-Hub/Campaigns/ParaguAI/brand/paraguai-logo.png
Use the EXACT logo: square icon (diagonal purple-pink gradient + white "AI"), wordmark "ParaguAI" (Paragu white, AI lavender on navy pill). Do NOT invent a new logo.

Background: dark navy #0F1419 like paragu-ai.com OG, or clean white.
Headline Spanish (max 8 words): "[HEADLINE DEL POST]"
Footer: paragu-ai.com in grey.
Rubro accent color only OUTSIDE the logo lockup.
See PARAGUAI-BRAND-GUIDE.md for full rules.
```

---

## Prompt — Variantes A/B (mismo creativo)

```text
Tengo este post base sobre ParaguAI:
[PEGAR POST]

Generá 3 variantes del hook (primera línea) manteniendo el mismo CTA.
Variante A: miedo a perder ventas
Variante B: facilidad / 48h
Variante C: prueba social 250+
Indicá cuál recomendás para Instagram Reels y por qué en 2 frases.
```

---

## Prompt — Respuesta a comentarios (bot / automatización)

```text
Sos el asistente de ParaguAI que redacta respuestas cortas para publicar automáticamente (o sugerir en cola de moderación). Respondé este comentario en español paraguayo, máx 2 frases, amable y sin presión:

Comentario: "[PEGAR]"

Si preguntan precio: mencioná Starter gratis y Profesional desde Gs. 650.000 setup + mensualidad, invitá a WhatsApp para demo.
Si es skeptico: demo gratis + ver sitios reales en la web.
```
