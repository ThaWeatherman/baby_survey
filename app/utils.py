import hashlib


def hash_password(s):
    h = hashlib.sha256()
    h.update(s)
    return h.hexdigest()
