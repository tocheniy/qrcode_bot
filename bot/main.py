from pathlib import Path
from pyzbar import pyzbar 
from PIL import Image


img_path = Path('bot','qrcodes','qr-code.png') 


img = Image.open(img_path)

dec = pyzbar.decode(img)
print(dec)
