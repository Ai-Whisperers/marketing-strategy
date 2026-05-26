# Carrusel — Planes ParaguAI (5 slides · IG 4:5)

**Tamaño:** **1080×1350 px** (feed Instagram, ratio 4:5). **Colores:** alineados al CSS público de [paragu-ai.com](https://paragu-ai.com/) (slate-900 / slate-800, gradiente purple-500 → pink-500). **Layout:** plantilla tipo **anuncio**: fondo visual a **pantalla completa** dentro de la tarjeta (`side-NN.png` opcional o procedural), velo oscuro, **copy centrado** a ancho completo; CTA + logo abajo.

**Jerarquía tipográfica (script):** `TextRow.role` distingue `headline` (contorno + bold), `subtitle` (stack Medium/SemiBold y más separación respecto al titular vía `HEADLINE_TO_SUBTITLE_EXTRA_GAP`), `label` / `body` / `price`. Ver `scripts/build_carousel_planes_png.py`.

**PNG:** [assets/creativos/paraguai-carousel-planes-01.png](assets/creativos/paraguai-carousel-planes-01.png) … [05](assets/creativos/paraguai-carousel-planes-05.png).

**Imágenes opcionales (columna derecha):** [assets/creativos/carousel-planes/README.md](assets/creativos/carousel-planes/README.md) (`side-01.png` … `side-05.png`).

**Regenerar:**

```bash
pip install -r scripts/requirements-creativos.txt
python scripts/build_carousel_planes_png.py
# opcional: genera *-layout-debug.png (mismos slides, contornos copy / CTA / logo)
python scripts/build_carousel_planes_png.py --layout-debug
```

**Planes y precios** (nombres y cifras como en la sección “Elegí tu plan” de [paragu-ai.com](https://paragu-ai.com/) el 2026-05):

| Plan | Setup | Mensual |
|------|--------|---------|
| **Starter** | Gratis | Subdominio · demo 3 meses |
| **Profesional** | Gs. 650.000 | + Gs. 100.000 / mes |
| **Negocio** | Gs. 1.200.000 | + Gs. 150.000 / mes |
| **A medida** (multi-sucursal / avanzado) | Gs. 2.200.000 | + Gs. 300.000 / mes |

---

## Storyboard (contenido por slide)

| Slide | Archivo | Rol |
|-------|---------|-----|
| 1 | `paraguai-carousel-planes-01.png` | Hook del sitio: “Tu negocio vendiendo mientras dormís” + valor 48h / todo incluido + CTA `paragu-ai.com` |
| 2 | `paraguai-carousel-planes-02.png` | **Starter** — qué incluye (subdominio, página, WhatsApp, 3 meses) + CTA **Empezar gratis** |
| 3 | `paraguai-carousel-planes-03.png` | **Profesional** — badge **Más elegido** (como en la web) + precios + lista de inclusiones + CTA **Elegir Profesional** |
| 4 | `paraguai-carousel-planes-04.png` | **Negocio** — precios + qué suma vs Profesional + CTA **Elegir Negocio** |
| 5 | `paraguai-carousel-planes-05.png` | **Plan a medida** (varias sucursales / complejidad) + precios 2.2M + 300k + **Hablar con ventas** |

**Logo:** `brand/paraguai-logo.png` en la franja inferior centrada.

**UTM sugerida:** `utm_source=instagram&utm_medium=organic&utm_campaign=carousel_planes_2026`
