import qrcode

# Define la URL de la página web
url = "https://sarasendi.github.io/SSendino.github.io/"

# Crea un objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agrega la URL al código QR
qr.add_data(url)
qr.make(fit=True)

# Crea una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen en un archivo
img.save("C:/Users/saras/Documents/Codigos_cursos/GIT/perfil/codigo_qr.png")