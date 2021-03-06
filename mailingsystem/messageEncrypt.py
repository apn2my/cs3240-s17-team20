from Crypto.Cipher import AES
import base64

MASTER_KEY='6(ri+i!%emkku*u%-$f1k1#-0&4m9aou^e#e(h7w0@6ch#9o7&'

def encrypt_val(clear_text):
    enc_secret = AES.new(MASTER_KEY[:32])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))

    return cipher_text


def decrypt_val(cipher_text):
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val = raw_decrypted.rstrip(b"\0")
    clear_val = str(clear_val)
    clear_val = clear_val[2:]
    clear_val = clear_val[:-1]
    return clear_val