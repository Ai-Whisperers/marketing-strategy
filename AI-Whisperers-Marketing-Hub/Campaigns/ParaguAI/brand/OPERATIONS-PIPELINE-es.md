# Operaciones y pipeline — ParaguAI

Define **estándares de proceso** desde el brief hasta la publicación, para equipos humanos o **automatización** (generación → QA → upload).

---

## 1. Mapa de artefactos

| Etapa | Entrada | Salida | Responsable |
|-------|---------|--------|---------------|
| P0 Brief | Objetivo del slot (calendario) | `verticals/{slug}/README.md` + pilar (dolor / prueba / CTA) | Estrategia / scheduler |
| P1 Copy | `03-social-post-prompts-es.md`, `04-*` few-shot | Caption + overlays por slide / guion reel | IA + reglas copy |
| P2 Imagen brief | `brand/image-prompts/WORKFLOW-pre-imagen-es.md` | `verticals/{slug}/image-prompt-es.md` aprobado | Revisor marca |
| P3 Render | `paraguai-logo.png` como referencia | `assets/creativos/vertical-<slug>-social-1080.png` (o ratio definido) | IA / diseño |
| P4 QA | Checklists abajo | Pieza “lista para cola” | Pipeline o humano |
| P5 Publicación | Cola + ventana horaria | Post live + URL final | Conector IG |
| P6 Medición | Insights + CRM | Fila en export métricas | Analytics |

---

## 2. Definition of Done (DoD) — un post feed

Se considera **completado** solo si:

1. Existe **slug de vertical** o pieza corporativa documentada en `02-marketing-plan-es.md` / calendario.
2. **URL de demo** coincide con [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md) (path canónico).
3. **UTM** incluye `utm_source`, `utm_medium=organic`, `utm_campaign` alineado al slug o a la semana.
4. **Creativo** cumple [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md) y [INSTAGRAM-STANDARDS-es.md](INSTAGRAM-STANDARDS-es.md).
5. **Copy** cumple regla sin “Google” (`.cursor/rules/campaigns/paraguai-copy-language-rule.mdc`).
6. Hay **captura o log** de publicación (id interno, timestamp) para trazabilidad.

---

## 3. Prioridades en conflicto

1. Veracidad respecto al sitio oficial.  
2. Marca (logo + nombre).  
3. Deep link correcto al vertical.  
4. Estética del rubro.

Si un dato del rubro en README local difiere del sitio en producción, **gana producción**; actualizar README en la misma tarea.

---

## 4. Versionado de prompts

- Cambios en `image-prompt-es.md` que afecten texto en imagen: incrementar nota de fecha al pie del archivo o en changelog interno del equipo.
- No regenerar masivamente PNG sin re-ejecutar checklist **pre-generación** en ese archivo.

---

## 5. Incidentes (creativo incorrecto)

1. Bajar pieza o reemplazar por placeholder corporativo si el error es de marca.  
2. Abrir tarea: captura + URL + qué regla se violó.  
3. Ajustar prompt o regla para que no se repita.

---

## 6. Archivos fuente de verdad

| Tema | Archivo |
|------|---------|
| Demos y URLs | [VERTICAL-DEMOS.md](VERTICAL-DEMOS.md) |
| Instagram | [INSTAGRAM-STANDARDS-es.md](INSTAGRAM-STANDARDS-es.md) |
| Marca visual | [PARAGUAI-BRAND-GUIDE.md](PARAGUAI-BRAND-GUIDE.md) |
| Calendario semanal / mensual | [../02-marketing-plan-es.md](../02-marketing-plan-es.md) |
| Prompts IA | [../03-social-post-prompts-es.md](../03-social-post-prompts-es.md) |
| PNG sociales (carpeta única) | [../assets/creativos/README.md](../assets/creativos/README.md) |
