# pip install pycryptodome 
from Crypto.Cipher import AES
key = b'C&F)H@McQfTjWnZr'
cipher = AES.new(key, AES.MODE_EAX)
data = "Welcome to copyassignment.com!".encode()
nonce = cipher.nonce
# encrypt the data
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext)
#decryption
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
# decrypt the data
decrypt= cipher.decrypt(ciphertext)
print("Plain text:", decrypt)

Import os
Import pyaes
# Generate a random 128-bit (16-byte) AES key
Key = os.urandom (16)
# Create an AES cipher object
Aes = pyaes.AESModeOfOperationCTR(key)
# Plaintext to encrypt
Plaintext = "hello world"
# Encrypt the plaintext
cipherText = aes. encrypt(plaintext. encode('utf-8')) # Encode plaintext as bytes
# Decrypt the ciphertext
Decrypted = aes.decrypt(cipherText). decode(utf-8') # Decode the decrypted bytes to string
Print("Original plaintext:", plaintext)
Print(Encrypted ciphertext:", rep(cipherText))
Print"Decrypted plaintext:", decrypted)
