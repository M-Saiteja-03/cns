def encrypt(m,s):
    res = ""
    for item in m:
        if item.isupper():
            res = res + chr((ord(item)+s-65)%26 +65)
        else:
            res = res + chr((ord(item)+s-97)%26 +97)
    return res
def decrypt(ciphertext, s):
    res = ""
    for item in ciphertext:
        if item.isupper():
            res = res + chr((ord(item) - s - 65) % 26 + 65)
        else:
            res = res + chr((ord(item) - s - 97) % 26 + 97)
    return res

m=input("Enter plaintext: ")
s=int(input("Enter shift: "))
e=encrypt(m,s) 
print("Encryption: ",e)
d=decrypt(e,s)
# d=encrypt(e,26-s)
print("Decryption: ",d)

'''
from pycipher import Caesar
plaintext = "Instrument"     
print("Plain text:",plaintext)
shift=3
cipher = Caesar(shift)
encrypted_text = cipher.encipher(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decipher(encrypted_text)
print("Decrypted:",decrypted_text)
'''