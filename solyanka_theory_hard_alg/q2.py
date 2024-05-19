"""
Разработайте программу, которая применяет алгоритм шифрования (например, алгоритм RSA) для защиты конфиденциальной
информации. Программа должна шифровать и расшифровывать сообщения, обеспечивая безопасность передачи данных.
"""
#pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(message, public_key):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return binascii.hexlify(encrypted_message).decode('utf-8')

def decrypt_message(encrypted_message, private_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(binascii.unhexlify(encrypted_message))
    return decrypted_message.decode('utf-8')

def main():
    private_key, public_key = generate_keys()
    message = input("Введите сообщение для шифрования: ")
    encrypted_message = encrypt_message(message, public_key)
    print(f"Зашифрованное сообщение: {encrypted_message}")
    decrypted_message = decrypt_message(encrypted_message, private_key)
    print(f"Расшифрованное сообщение: {decrypted_message}")

if __name__ == "__main__":
    main()

