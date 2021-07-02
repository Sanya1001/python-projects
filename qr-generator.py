# This code generates a QR code for my Github profile
# Modify the link to suit your needs

import sys


def qr_generator(link):
    import pyqrcode
    from pyqrcode import QRCode

    #link = 'https://github.com/Sanya1001'
    url = pyqrcode.create(link)
    url.svg('git.svg', scale=8)

n=len(sys.argv)
link = 'https://github.com/Sanya1001'
if(n>1):
	link=sys.argv[1]
print ("Using link")
print(link)
qr_generator(link)
