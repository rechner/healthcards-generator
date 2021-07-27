import sys
import base64
from io import BytesIO

from PIL import Image
from pyzbar import pyzbar
from healthcards import parser, cvx
from jinja2 import Environment, PackageLoader, select_autoescape
import qrcode

import fhirclient.models.bundle as b
from fhirclient import models


def human_name(human_name_instance):
    if human_name_instance is None:
        return "???"

    parts = []
    for n in [human_name_instance.prefix, human_name_instance.given]:
        if n is not None:
            parts.extend(n)
    if human_name_instance.family:
        parts.append(human_name_instance.family)
    if human_name_instance.suffix and len(human_name_instance.suffix) > 0:
        if len(parts) > 0:
            parts[len(parts) - 1] = parts[len(parts) - 1] + ','
        parts.extend(human_name_instance.suffix)

    return ' '.join(parts) if len(parts) > 0 else 'Unnamed'

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <qr code image>")
    exit()

# Decode QR code
barcode_data = pyzbar.decode(Image.open(sys.argv[1]))

if len(barcode_data) == 0:
    print("Unable to decode any QR codes :(")
    exit()

# Unpack SHC payload to a JWS
jws_str = parser.decode_qr_to_jws(barcode_data[0].data.decode())

#print(jws_str)

# Decode the JWS
jws = parser.JWS(jws_str)

shc_dict = jws.as_dict()

import pprint; pprint.pprint(shc_dict)
