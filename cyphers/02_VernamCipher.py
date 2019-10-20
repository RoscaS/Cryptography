"""
Exercise 2: Vernam cyper
"""
import binascii

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = [str(x) for x in range(10)]
chars = numbers + letters

def vernam_cipher_encrypt(D, key):
    idx = 0
    E = ""
    for char in D:
        E = E + chr(ord(char) ^ ord(key[idx]))
        idx = 0 if idx == len(key) - 1 else idx + 1
    return bin(int(binascii.hexlify(E), 16))

def vernam_cipher(message, key):
    print(f"The text {message} and the key {key}")
    word = ""
    for i in range(len(message)):
        bin1 = str(bin(chars.index(message[i])))[2:][::-1]  # MSB -> right
        bin2 = str(bin(chars.index(key[i])))[2:][::-1]  # MSB -> right
        cpt = ""
        for j in range(max(len(bin1), len(bin2))):
            t = 0
            if j < len(bin1):
                t = int(bin1[j])
            if j < len(bin2):
                t += int(bin2[j])
            cpt = str(t % 2) + cpt  # Add MSB o the left
        word += chars[
            int(cpt, 2) % 16]  # %16 (hex)
    print(f"The ciphertext is : {word}")




if __name__ == '__main__':
    vernam_cipher("9AC3", "6B9D")

