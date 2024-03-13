def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input(" Hello Ceaser Cipher \n Do you want to encrypt or decrypt a message? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'encrypt':
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print("Decrypted text:", decrypted_text)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
