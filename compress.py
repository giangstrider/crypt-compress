import os
import io
import gnupg
from pprint import pprint
import gzip
import zipfile




def gzip_decompress(crypted_data):
    crypted_data = io.BytesIO(crypted_data)
    decompressed_data = gzip.GzipFile(fileobj=crypted_data)
    return decompressed_data

def zip_compress(crypted_data, name_inside, in_memory=True):
    if in_memory:
        mem_zip = io.BytesIO()
        with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(name_inside, crypted_data)
            zf.printdir()
            zf.close()

        return mem_zip.getvalue()

### GZIP, ZIP, 7z
# def gzip_compress():
# def gzip_decompress():        
