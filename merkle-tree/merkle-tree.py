from hashlib import sha1


def hashing_helper_function(string):
    return sha1(string.encode()).hexdigest()


digest_1 = hashing_helper_function("Bloque 1")
digest_2 = hashing_helper_function("Bloque 2")

root = hashing_helper_function(digest_1+digest_2)

print(root)
