import os
import gnupg
from pprint import pprint

def init(key_path):
    homedir = './' + key_path
    gpg = gnupg.GPG(
        gnupghome=homedir
    )
    return gpg

def import_key(key_path, key_file, is_private_key=True):
    gpg = init(key_path)
    key_data = open(key_file).read()
    import_result = gpg.import_keys(key_data)
    
    pprint(import_result.results)

    keys = gpg.list_keys(is_private_key)
    finger_print = None
    if not is_private_key:
        finger_print = keys[0]['fingerprint']

    return {"gpg": gpg, "finger_print": finger_print}

def crypt_handler(crypt_data):
    if crypt_data.ok:
        crypt_data = crypt_data.data
    else:
        raise Exception(crypt_data.stderr)    

def encrypt(gpg, finger_print, bytes_content, output=None, trust_key=True):
    if output:
        encrypted_data = gpg.encrypt(bytes_content, finger_print, always_trust=trust_key, output=output)
    else:
        encrypted_data = gpg.encrypt(bytes_content, finger_print, always_trust=trust_key)
    return crypt_handler(encrypted_data)

def decrypt(gpg, passphrase, bytes_content, output=None):
    if output:
        decrypted_data = gpg.encrypt(bytes_content, passphrase, output=output)
    else:
        decrypted_data = gpg.encrypt(bytes_content, passphrase)
    return crypt_handler(decrypted_data)


key_name = os.getenv("SAMPLE_KEY_NAME", "gpg")