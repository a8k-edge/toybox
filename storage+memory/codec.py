import os
import glob
import argparse
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def load_key(key_file):
    with open(key_file, 'rb') as f:
        return f.read()


def save_key(key_file, key):
    with open(key_file, 'wb') as f:
        f.write(key)


def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = Fernet(key).encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt Markdown files.')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform (encrypt or decrypt)')
    parser.add_argument('--key-file', default='.key', help='File to store/load encryption key')
    parser.add_argument('--dir', default='./', help='Directory containing markdown files')

    args = parser.parse_args()

    if args.action == 'encrypt':
        key = generate_key()
        save_key(args.key_file, key)
    else:
        key = load_key(args.key_file)

    markdown_dir = args.dir

    if args.action == 'encrypt':
        for file in glob.glob(os.path.join(markdown_dir, '*.md')):
            encrypt_file(file, key)
    else:
        for file in glob.glob(os.path.join(markdown_dir, '*.md')):
            decrypt_file(file, key)
