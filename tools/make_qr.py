"""Genera assets/qr.png (web) y assets/qr-imprimir.png (alta resolución) para la URL dada.
Uso: python tools/make_qr.py https://tu-url-publicada
"""
import sys, qrcode
from qrcode.constants import ERROR_CORRECT_H
url = sys.argv[1]
for name, box in (("assets/qr.png", 8), ("assets/qr-imprimir.png", 30)):
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=box, border=3)
    q.add_data(url); q.make(fit=True)
    q.make_image(fill_color="#1f3a1f", back_color="white").save(name)
print("QR ->", url)
