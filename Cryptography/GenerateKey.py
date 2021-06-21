from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("encryption_key.text", "wb")
file.write(key)
file.close()