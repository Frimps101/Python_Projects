import qrcode
import decode
from PIL import Image

# data = "Hello, world"

# Encoding

# img = qrcode.make(data)

# img.save("C:/python_scripts/six_python_projects/data/myqrcode.png")

# qr = qrcode.QRCode(version=1, box_size=10, border=5)

# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill_color="red", back+color="white")
# img.save(fit=True)


# Decoding
img = Image.open("C:/python_scripts/six_python_projects/data/myqrcode.png")

result = decode(img)
