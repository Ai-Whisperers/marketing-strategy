# Fuentes locales (creativos raster)

Los `.ttf` en esta carpeta **no se versionan** (ver `.gitignore` aquí mismo): cada máquina o CI copia las fuentes con licencia adecuada.

**Norma de uso:** [TYPOGRAPHY-POST-STANDARD-es.md](../TYPOGRAPHY-POST-STANDARD-es.md) · **Script:** `scripts/build_carousel_planes_png.py` (busca primero `brand/fonts/`, luego `PARAGUAI_FONT_DIR`, luego fuentes del sistema).

---

## Descargas oficiales (SIL / OFL)

| Familia | Licencia | Dónde descargar |
|---------|----------|-----------------|
| **Inter** | SIL OFL 1.1 | [Releases — rsms/inter](https://github.com/rsms/inter/releases) → asset *Inter-X.Y.zip* → carpeta `extras/ttf` o estáticos con prefijo `Inter_18pt-*.ttf`. También en [Google Fonts — Inter](https://fonts.google.com/specimen/Inter) → “Download family” → carpeta `static/`. |
| **Plus Jakarta Sans** | SIL OFL | [Google Fonts](https://fonts.google.com/specimen/Plus+Jakarta+Sans) → Download family → `static/*.ttf`. |
| **Montserrat** | SIL OFL | [Google Fonts](https://fonts.google.com/specimen/Montserrat) → Download family → `static/*.ttf`. |
| **DM Sans** | SIL OFL | [Google Fonts](https://fonts.google.com/specimen/DM+Sans) → Download family → `static/*.ttf`. |

Revisá siempre el archivo `LICENSE.txt` / `OFL.txt` del ZIP antes de redistribuir creativos derivados en otro canal.

---

## Nombres que reconoce el script (renombrá si hace falta)

El carrusel **no** abre fuentes variable (`*VariableFont*.ttf`): usá archivos **estáticos** por peso.

### Inter (prioridad 1)

| Peso | Nombres aceptados (cualquiera sirve; el script prueba en orden) |
|------|-------------------------------------------------------------------|
| Bold | `inter-bold.ttf`, `Inter-Bold.ttf`, `Inter_18pt-Bold.ttf` |
| SemiBold | `inter-semibold.ttf`, `Inter-SemiBold.ttf`, `Inter_18pt-SemiBold.ttf` |
| Medium | `inter-medium.ttf`, `Inter-Medium.ttf`, `Inter_18pt-Medium.ttf` |
| Regular | `inter-regular.ttf`, `Inter-Regular.ttf`, `Inter_18pt-Regular.ttf` |

### Plus Jakarta Sans

Bold: `PlusJakartaSans-Bold.ttf` · SemiBold: `PlusJakartaSans-SemiBold.ttf` · Medium: `PlusJakartaSans-Medium.ttf` · Regular: `PlusJakartaSans-Regular.ttf`

### DM Sans

Bold: `DMSans-Bold.ttf` o `DM-Sans-Bold.ttf` · SemiBold / Medium / Regular: mismo patrón (`DMSans-*.ttf` o `DM-Sans-*.ttf`).

### Montserrat

`Montserrat-Bold.ttf`, `Montserrat-SemiBold.ttf`, `Montserrat-Medium.ttf`, `Montserrat-Regular.ttf`

### Fallback (Windows)

Si no hay ningún `.ttf` en esta carpeta, el script puede usar `segoeuib.ttf` / `segoeui.ttf` o `arialbd.ttf` / `arial.ttf` desde `C:\Windows\Fonts`.

---

## Conjunto mínimo recomendado (un solo carrusel “pro”)

Para que coincidan **titular (bold)**, **subtítulo (medium/semibold)** y **cuerpo (regular)** sin depender del sistema:

1. **Inter:** al menos `Inter_18pt-Bold.ttf`, `Inter_18pt-Medium.ttf`, `Inter_18pt-Regular.ttf` (y opcional `Inter_18pt-SemiBold.ttf`).
2. Copiá esos archivos **tal cual el nombre** en `Campaigns/ParaguAI/brand/fonts/`.

Si solo copiás **Regular + Bold**, el subtítulo caerá a Regular (sigue siendo legible).

---

## Cómo probar

Desde la raíz de la campaña ParaguAI:

```bash
pip install -r scripts/requirements-creativos.txt
python scripts/build_carousel_planes_png.py
```

Salida: `assets/creativos/paraguai-carousel-planes-01.png` … `05.png`. Opcional: `--layout-debug` para contornos de zonas.

---

## Variable de entorno

`PARAGUAI_FONT_DIR` apuntando a otra carpeta con `.ttf` tiene **prioridad** sobre `brand/fonts/` (útil en CI o si centralizás fuentes fuera del repo).
