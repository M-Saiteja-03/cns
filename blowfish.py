from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

# Generate a random encryption key (must be 16, 24, or 32 bytes long)
key = get_random_bytes(16)

# Create a Blowfish cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # ECB mode is used for simplicity; use other modes for better security

# Text to be encrypted (must be a multiple of 8 bytes for ECB mode)
plaintext = b'Hello, Blowfish!'

# Encrypt the text
ciphertext = cipher.encrypt(plaintext)

# Decrypt the text
decrypted_text = cipher.decrypt(ciphertext)

# Print the results
print("Original text:", plaintext.decode())
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_text.decode())

'''
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_text(key, plaintext):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_plaintext = pad(plaintext, Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_text(key, ciphertext):
    decipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_text = decipher.decrypt(ciphertext)
    original_plaintext = unpad(decrypted_text, Blowfish.block_size)
    return original_plaintext

# Generate a random 64-bit (8-byte) Blowfish key
key = get_random_bytes(8)

# Define the new plaintext to be encrypted
new_plaintext = b"This is a different plaintext."

# Encrypt the plaintext
encrypted_data = encrypt_text(key, new_plaintext)

# Decrypt the ciphertext
decrypted_data = decrypt_text(key, encrypted_data)

# Print the results
print("Original plaintext:", new_plaintext)
print("Encrypted ciphertext:", encrypted_data)
print("Decrypted text:", decrypted_data.decode("utf-8"))

**BlowFish**
'''
