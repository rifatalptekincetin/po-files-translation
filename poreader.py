from babel.messages.pofile import read_po,write_po
from babel._compat import StringIO

def get_po(path,encoding="utf-8"):
    with open(path,"r",encoding=encoding) as f:
        file=StringIO(f.read())

    return read_po(file)

def save_po(po,path):
    with open(path,"wb") as f:
        write_po(f, po, omit_header=True)
