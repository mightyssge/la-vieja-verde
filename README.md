# La Vieja Verde · espacio digital (Grupo 4)

Página de una sola pantalla (`index.html`) para la exposición: historia, 3 sabores, ingredientes,
información nutricional, atributos, trazabilidad QR, mercado alemán y proceso de exportación.
Idiomas ES / DE / EN (botones arriba a la derecha, o `?lang=de` en la URL).

## Antes de exponer
Publicado en **https://mightyssge.github.io/la-vieja-verde/** (GitHub Pages, se actualiza con cada push a `main`).
El QR (`assets/qr.png`, `assets/qr-imprimir.png`) ya apunta a esa URL.

1. **Video de exportación (opcional)**: guardar el archivo como `video/exportacion.mp4` y poner
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

## Ver en local
```
python -m http.server 5510
```
y abrir http://localhost:5510

## Notas de datos
- Fuentes: TB3_Grupo04.xlsx, rúbrica del grupo, PPT Canva, laviejaverdeperu.com.
- Nutrición: Lucumaní según ficha técnica (energía, grasas, hidratos, azúcares, proteínas).
  Chocomaní, Cafemaní, grasas saturadas y fibra son valores calculados por formulación (indicado en la página).
