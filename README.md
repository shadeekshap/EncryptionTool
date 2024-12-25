# EncryptionTool

# Basic Encryption/Decryption Tool

This is a simple encryption and decryption tool implemented in Python using Caesar Cipher and AES encryption algorithms.

## Features
- Encrypts and decrypts text using Caesar Cipher.
- Supports AES encryption for secure text handling.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/shadeekshap/EncryptionTool.git

2. Install dependencies:
   ```bash
   pip install cryptography

3. Run the encryption tool:
   ```bash
   python encryption_tool.py

4. To encrypt or decrypt, follow the prompts in the terminal.

5. You will need to provide a shift value for the Caesar Cipher.


## Example Usage:
To encrypt text using Caesar Cipher:
   ```bash
   Do you want to (E)ncrypt or (D)ecrypt? e
   Enter the text: Hello World!
   Enter shift value: 3
   Encrypted: Khoor Zruog!
   ```

To decrypt the encrypted text:
   ```bash
   Do you want to (E)ncrypt or (D)ecrypt? d
   Enter the text: Khoor Zruog!
   Enter shift value: 3
   Decrypted: Hello World!
   ```

## Requirements
- Python 3.x
- Install dependencies: pip install cryptography

## License
This project is licensed under the MIT License.