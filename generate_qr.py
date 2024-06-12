import qrcode

# URL of your GIF
## Download
# gif_url = 'https://raw.githubusercontent.com/Marcony1/dsensegif/main/demo.gif'
## Visualize
gif_url = 'https://github.com/Marcony1/dsensegif/blob/main/demo.gif'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(gif_url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save('results/qrcode.png')
