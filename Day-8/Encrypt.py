alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encrypt_txt = ""
    for c in text:
        index = alphabet.index(c)
        shift_index = index + shift
        encrypt_txt += alphabet[shift_index]
    print(f"Encrypted Text is {encrypt_txt}")


def decrypt(text, shift):
    decrypt_txt = ""
    for c in text:
        index = alphabet.index(c)
        shift_index = index - shift
        decrypt_txt += alphabet[shift_index]
    print(f"Decrypted Text is {decrypt_txt}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text=text, shift=shift)
else:
    decrypt(text=text, shift=shift)
