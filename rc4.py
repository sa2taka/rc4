# reffer: https://tools.ietf.org/html/draft-kaukonen-cipher-arcfour-03
def setup_key(key):
    keylen = len(key)
    s = range(256)
    j = 0
    for i in range(256):
        j = (j + s[i] + ord(key[i % keylen])) % 256
        s[i], s[j] = s[j], s[i]
    return s


def generate_stream(s):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        yield k


def rc4(data, key):
    s = setup_key(key)
    gen = generate_stream(s)
    encrypted = bytearray(c ^ n for c, n in zip(bytearray(data), gen))
    return str(encrypted)


if __name__ == '__main__':
    key = 'this_is_a_key'
    data = 'this_is_a_plain_text'
    encrypted = rc4(data, key)
    print(encrypted)
    decrypted = rc4(encrypted, key)
    print(decrypted)
