import string

letters = [c for c in string.ascii_uppercase]
numbers = [str(x) for x in range(10)]
tab = numbers + letters


def vernam_cipher(message, key):
    ''' Exercice 2 '''
    print(f"The text {message} and the key {key}")
    word = ""
    for i in range(len(message)):
        bin1 = str(bin(tab.index(message[i])))[2:][::-1]  # MSB -> right
        bin2 = str(bin(tab.index(key[i])))[2:][::-1]  # MSB -> right
        cpt = ""
        for j in range(max(len(bin1), len(bin2))):
            t = 0
            if j < len(bin1):
                t = int(bin1[j])
            if j < len(bin2):
                t += int(bin2[j])
            cpt = str(t % 2) + cpt  # Add MSB o the left
        word += tab[
            int(cpt, 2) % 16]  # %16 (hex)
    print(f"The ciphertext is : {word}")


if __name__ == '__main__':
    vernam_cipher("9AC3", "6B9D")
