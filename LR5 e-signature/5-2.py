import rsa
from hashlib import sha256


def hash_file(filename):
    h = sha256() 
    with open(filename, "rb") as f: 
        while True:
            buf = f.read(1024) 
            if len(buf) == 0:
                break
            h.update(buf) 
    return h.digest() 


def make_signature(filename, private_key):
    h = hash_file(filename)

    signature = rsa.sign(h, private_key, 'SHA-256')

    signature_filename = 'signature_test.txt'
    with open(signature_filename, "wb") as f:
        f.write(signature)


def check_signature(filename, signature_file, public_key):
    h1 = hash_file(filename)

    with open(signature_file, "rb") as f:
        signature = f.read()
    try:
        rsa.verify(h1, signature, public_key)
        print("Digital Signature is verified")
        return 0
    except rsa.pkcs1.VerificationError:
        print("Digital Signature is not verified")
        return 1

def main():
    filename = 'test.txt'
    (open_key, private_key) = rsa.newkeys(1024)

    make_signature(filename, private_key)
    print("Digital Signature is done")

    signature_filename = 'signature_test.txt'  #+ '.txt'
    is_verified = check_signature(filename, signature_filename, open_key)


if __name__ == '__main__':
    main()
