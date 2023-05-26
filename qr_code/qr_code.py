import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# --- Simple usage
data = """
		Steven George Gerrard, MBE (kiejtése: 'stiːvn 'ʤɛɹaːd) (Whiston, 1980. május 30.) angol labdarúgó, középpályás. 
		Korábban a Liverpool FC, illetve az angol labdarúgó-válogatott csapatkapitánya. Pályafutásának utolsó két évét az 
		amerikai Los Angeles Galaxy-nál töltötte. 2016. november 24-én jelentette be visszavonulását. Korábban az angol 
		Aston Villa és a skót Rangers edzője.
		"""
img = qrcode.make(data)
img.save('sg8.png')

# --- More complex one

#qr = qrcode.QRCode(version=1,box_size=10,border=5) # parameterize its size
#qr.add_data(data)
#qr.make(fit=True)
#img = qr.make_image(fill_color='red',back_color='white') # parameterize its color comps
#img.save('sg8_red.png')

# --- Encoding QR-s

image = Image.open('sg8.png')
result = decode(image)
print(result)


