# La Vieja Verde · espacio digital (Grupo 4)

Página de una sola pantalla (`index.html`) para la exposición: historia, 3 sabores, ingredientes,
información nutricional, atributos, trazabilidad QR, mercado alemán y proceso de exportación.
Idiomas ES / DE / EN (botones arriba a la derecha, o `?lang=de` en la URL).

## Antes de exponer
Publicado en **https://mightyssge.github.io/la-vieja-verde/** (GitHub Pages, se actualiza con cada push a `main`).
El QR (`assets/qr.png`, `assets/qr-imprimir.png`) ya apunta a esa URL.

1. **Video de exportación**: `video/exportacion.mp4` (38 s) se hizo con HyperFrames; el proyecto fuente está en `../la-vieja-verde-video/` (`npm run check`, `npm run render -- -o ../la-vieja-verde/video/exportacion.mp4`).
   Para reemplazarlo por otro video: guardar el archivo como `video/exportacion.mp4` y poner
   `VIDEO_FILE = "video/exportacion.mp4"` en `index.html`, o pegar un enlace en `VIDEO_YOUTUBE`.
   Ajustar `CHAPTER_TIMES` a los segundos reales. Sin video, se muestra la ruta animada.
2. **Si cambia la URL**, regenerar el QR:
   ```
   python tools/make_qr.py https://TU-URL
   ```
   Genera `assets/qr.png` (web) y `assets/qr-imprimir.png` (alta resolución para imprimir).

## Durante la exposición
- Flechas ← → del teclado: saltar de sección en sección.
- Sección Exportación: botón «Reproducir recorrido» anima la ruta Lima → Callao → Panamá → Hamburgo.
- Trazabilidad: probar los lotes de ejemplo CH-2028-009, CF-2028-011, LU-2028-014.
- El selector de sabor (Chocomaní / Cafemaní / Lucumaní) cambia el color de toda la página.
  Para abrir directo en un sabor: `?f=choco`, `?f=cafe` o `?f=lucu` (combinable con `&lang=de`).

## Imágenes
Fotos de producto y ambiente generadas con IA (Higgsfield, GPT Image 2.6) usando como referencia
la foto real del frasco de 220 g de laviejaverdeperu.com. Fondos recortados con el removedor de Higgsfield.

## Ver en local
```
python -m http.server 5510
```
y abrir http://localhost:5510

## Notas de datos
- Fuentes: TB3_Grupo04.xlsx, rúbrica del grupo, PPT Canva, laviejaverdeperu.com.
- Nutrición: Lucumaní según ficha técnica (energía, grasas, hidratos, azúcares, proteínas).
  Chocomaní, Cafemaní, grasas saturadas y fibra son valores calculados por formulación (indicado en la página).
