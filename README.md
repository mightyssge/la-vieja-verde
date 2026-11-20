# La Vieja Verde · espacio digital (Grupo 4)

Página de una sola pantalla (`index.html`) para la exposición: historia, 3 sabores, ingredientes,
información nutricional, atributos, trazabilidad QR, mercado alemán y proceso de exportación.
Idiomas ES / DE / EN (botones arriba a la derecha, o `?lang=de` en la URL).

## Antes de exponer
1. **Video de exportación**: guardar el video como `video/exportacion.mp4`
   (o pegar el enlace de YouTube en `VIDEO_YOUTUBE`, dentro de `index.html`).
   Ajustar `CHAPTER_TIMES` a los segundos reales de cada etapa del video.
2. **Publicar** la carpeta completa (Netlify Drop: arrastrar la carpeta en https://app.netlify.com/drop,
   o GitHub Pages).
3. **QR definitivo** con la URL publicada:
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
