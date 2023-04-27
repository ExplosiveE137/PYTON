import hashlib


def md5(N):
    hash_object = hashlib.md5(N.encode('utf-8'))
    return hash_object.hexdigest()
