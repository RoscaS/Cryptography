"""
Exercise 1: Vigenère cyper
"""

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Ki = lambda c, k: letters.index(k[c % len(k)])


def viginere_cipher_encrypt(D, key):
    """Encrypt: Ei = (Pi + Ki) % 26"""
    Pi = lambda i: letters.index(i)
    Ei = lambda a, b: letters[(a + b) % 26]
    E = [Ei(Pi(i), Ki(c, key)) for c, i in enumerate(D)]
    return "".join(E)


def viginere_cipher_decode(E, key):
    """Decrypt: Di = (Ei - Ki + 26) % 26"""
    Di = lambda c, i: (letters.index(i) - Ki(c, key) + 26) % 26
    D = [letters[Di(c, i)] for c, i in enumerate(E)]
    return "".join(D)


def viginiere_test():
    key = "LEMON"
    plein = "ATTACKATDAWN"
    encrypted = "LXFOPVEFRNHR"
    assert viginere_cipher_encrypt(plein, key) == encrypted
    assert viginere_cipher_decode(encrypted, key) == plein


if __name__ == '__main__':
    viginiere_test()
    cipher_text = "HIMEZYZIPK"
    key = "GOOGLE"
    D = viginere_cipher_decode(cipher_text, key)
    print(D)
