# Function to encrypt a text using Caesar Cipher
def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabetic characters remain the same
    return encrypted_text

# Function to decrypt the text using Caesar Cipher
def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)  # Decrypt by shifting in the opposite direction

# Example usage
text = "Hello World!"
shift_value = 3
encrypted = encrypt_caesar(text, shift_value)
print(f"Encrypted: {encrypted}")
decrypted = decrypt_caesar(encrypted, shift_value)
print(f"Decrypted: {decrypted}")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    text = input("Enter the text: ")

    if choice == 'e':
        shift = int(input("Enter shift value: "))
        encrypted = encrypt_caesar(text, shift)
        print(f"Encrypted: {encrypted}")
    elif choice == 'd':
        shift = int(input("Enter shift value: "))
        decrypted = decrypt_caesar(text, shift)
        print(f"Decrypted: {decrypted}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()