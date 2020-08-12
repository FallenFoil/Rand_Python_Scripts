def encrypt():
    plain_text = input("Plaintext: ")
    plain_text = plain_text.upper()
    key = input("Key: ")
    key = key.upper()

    cipher_text = ""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    i = 0

    for char in plain_text:
        if char.isalpha():
            pi = ord(char) - 65
            ki = ord(key[i % len(key)]) - 65
            index = (pi + ki) % 26

            cipher_text = cipher_text + alphabet[index]
            i += 1
        else:
            cipher_text = cipher_text + char

    print(f"Ciphertext: {cipher_text}")


def decrypt():
    cipher_text = input("Ciphertext: ")
    cipher_text = cipher_text.upper()
    key = input("Key: ")
    key = key.upper()

    plain_text = ""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    i = 0

    for char in cipher_text:
        if char.isalpha():
            ci = ord(char) - 65
            ki = ord(key[i % len(key)]) - 65
            index = (ci - ki) % 26

            plain_text = plain_text + alphabet[index]
            i += 1
        else:
            plain_text = plain_text + char

    print(f"Plaintext: {plain_text}")


opt = 1

while True:
    print("1. Encryption\n2. Decryption")
    opt = input("$ ")

    try:
        opt = int(opt)

        if opt == 1 or opt == 2:
            break
    except:
        print("An error has occurred")

if opt == 1:
    encrypt()
else:
    decrypt()
