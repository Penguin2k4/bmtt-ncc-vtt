from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
import socket
import threading
import hashlib


server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',12345))
server_socket.listen(5)


server_key = RSA.generate(2048)


clients = []


def encrypt_message (key,encrypted_message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext= cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext