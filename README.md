Healthcards Generator
======
Decodes an SHC-formatted vaccine credential barcode and reformats it in a
suitable manner for printing on a CR-80 size card.

![example output](https://github.com/rechner/healthcards-generator/blob/main/doc/example_output.png?raw=true)


Quickstart
==========

    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    python svg_gen.py mybarcode.png output.svg
