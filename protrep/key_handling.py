from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey as PrivateKey
from cryptography.exceptions import InvalidSignature


def create_private_key(private_key_filename='key.pem', passphrase=None):
    """
    Create a new private key and store it in private_key_filename (defaults to 'key.pem', may be None for no file).
    Return public key
    """
    private_key = PrivateKey.generate()
    if private_key_filename:
        write_private_key(private_key, private_key_filename, passphrase)

    return private_key


def sign(text, private_key_filename=None, private_key=None):
    """
    Create a signature for text and return it. Either private_key or private_key_filename must be specified
    """
    assert (private_key_filename is not None) or (private_key is not None)
    private_key = read_private_key(private_key_filename) if private_key is None else private_key

    return private_key.sign(text.encode('utf-8')).hex()


def get_public_key_string_from_private_key(private_key):
    return private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH)


def get_public_key_from_string(public_key_string):
    return serialization.load_ssh_public_key(public_key_string)


def verify(text, public_key, signature_hex):
    """
    Return True if signature matches text
    """
    signature = bytearray.fromhex(signature_hex)
    try:
        public_key.verify(signature, text.encode('utf-8'))
        return True
    except InvalidSignature:
        return False


def write_private_key(private_key, filename, passphrase):
    if passphrase:
        encryption_algorithm = serialization.BestAvailableEncryption(passphrase.encode('utf-8'))
    else:
        encryption_algorithm = serialization.NoEncryption()

    with open(filename, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=encryption_algorithm))


def read_private_key(filename='key.pem'):
    with open(filename, 'rb') as f:
        return PrivateKey.from_private_bytes(f.read())
