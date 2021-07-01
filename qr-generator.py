# This code generates a QR code for my Github profile
# Modify the link to suit your needs

def qr_generator():
    import pyqrcode
    from pyqrcode import QRCode

    link = 'https://github.com/Sanya1001'
    url = pyqrcode.create(link)
    url.svg('git.svg', scale=8)


qr_generator()
