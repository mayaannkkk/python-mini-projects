import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

plain_text = input("Enter a message:")
cipher_text = ""

# Encrypt
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Your message:{plain_text:}")
print(f"Encrypted Message:{cipher_text}")

# Decrypt
choice = int(input("If you want to Decrypt the message type 1 else 0:"))
if choice == 1:
    cipher_text = input("Enter the Encrypted Message:")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Your Encrypted Message:{cipher_text:}")
    print(f"Decrypted Message:{plain_text}")
