import os
import gnupg
from pprint import pprint

key_name = os.getenv("SAMPLE_KEY_NAME", "gpg")
homedir = './' + key_name

gpg = gnupg.GPG(
    gnupghome=homedir
)

input_data = gpg.gen_key_input(
    name_email='strider.giang@live.com',
    passphrase='SamplePassphrase')

key = gpg.gen_key(input_data)

ascii_armored_public_keys = gpg.export_keys(key)
ascii_armored_private_keys = gpg.export_keys(key, True)
with open(homedir + '/{}-pub.asc'.format(key_name), 'w') as f:
    f.write(ascii_armored_public_keys)

with open(homedir + '/{}-pri.asc'.format(key_name), 'w') as f:
    f.write(ascii_armored_private_keys)