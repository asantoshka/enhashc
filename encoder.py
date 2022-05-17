import base64, hashlib
from Crypto.Hash import MD4
import urllib.parse

hash_funcs = {'md5' : hashlib.md5,  'sha1' : hashlib.sha1, 'sa224' : hashlib.sha224, 'sha256' : hashlib.sha256, 'sha384' : hashlib.sha384, 'sha512' : hashlib.sha512, 'sha3_224' : hashlib.sha3_224, 'sha3_256' : hashlib.sha3_256, 'sha3_384' : hashlib.sha3_384, 'sha3_512' : hashlib.sha3_512}


def encoder(ptext):
    result = {}
    result['base64'] = base64.standard_b64encode(ptext).decode("utf-8") 
    result['base32'] = base64.b32encode(ptext).decode("utf-8") 
    result['url'] = urllib.parse.quote(ptext)
    result['hex'] = str(ptext).encode('utf-8').hex()
    result['reverse'] = reverse(ptext)
    return result

def hasher(ptext):
    result = {}
    result['md4'] = hashlib.new('md4',ptext).hexdigest()
    for key in hash_funcs:
        result[key] = hash_funcs[key](ptext).hexdigest()
    return result

def hash_file(filename, func):
   h = func()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

def hash_func_itr(filename):
    result = {}
    for key in hash_funcs:
        func = hash_funcs[key]
        result[key] = hash_file(filename=filename,func=func)
    return result
        
def reverse(ptext):
    ptext = ptext.decode("utf-8") 
    rtext = ptext[::-1]
    return rtext

