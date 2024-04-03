from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


private_key_file = open("private.pem", "rb")
private_key = RSA.importKey(private_key_file.read())
private_key_file.close()

cipher = PKCS1_v1_5.new(private_key)

encrypted = cipher.encrypt(bytes("TEST_MASSAGE", "utf-8"))
print("Encrypted: ", encrypted.hex())

public_key_file = open("public.pem", "rb")
public_key = RSA.importKey(public_key_file.read())
public_key_file.close()

decryption = PKCS1_v1_5.new(public_key)
sentinel = get_random_bytes(16)

originalText = decryption.decrypt(encrypted, sentinel, expected_pt_len=16)
