import os
import sys

import qrcode


def generate_qr(text):
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=2
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')


def show_qr():
    os.system('qrcode.png')


if __name__ == '__main__':
    # check arguments
    if len(sys.argv) < 2:
        print("Please enter a url as an argument")
        exit()
    generate_qr(sys.argv[1])
    show_qr()
