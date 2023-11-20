import hashlib

text = "Your text goes here"
# Convert the text to bytes
text_bytes = text.encode('utf-8')

# Create a SHA-1 hash object
sha1_hash = hashlib.sha1()

# Update the hash object with the text bytes
sha1_hash.update(text_bytes)

# Get the SHA-1 digest in hexadecimal format
digest = sha1_hash.hexdigest()

print("SHA-1 Digest:", digest)

'''
def sha1(data):
    bytes = ""
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits
    while len(pBits)%512 != 448:
        pBits+="0"
    pBits+='{0:064b}'.format(len(bits)-1)
    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]
    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
    for c in chunks(pBits, 512): 
        words = chunks(c, 32)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp
        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff
    hex_hash = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    print("SHA (Hexadecimal): ", hex_hash)
    binary_result = bin(int(hex_hash, 16))[2:]
    return binary_result
str=input("Enter the string: ")
print ("SHA (Binary): ", sha1(str))
'''