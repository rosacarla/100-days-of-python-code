#Gerador de QR Code - simples

import pyqrcode

codigo = pyqrcode.create("https://cutt.ly/LyvJwYj")

codigo.png("codigo.png",scale=6)

if codigo != 0:
    print("QR Code gerado!")
