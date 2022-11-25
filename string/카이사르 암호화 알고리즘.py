def encipher(plain, k):
    n = len(plain)
    cipher = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32: a = 64
        t = a + k
        if t > 90: t -= 27
        if t == 64: t = 32
        cipher += chr(t)
    return cipher
    
plainText = 'SAVE PRIVATE RYAN'
K = 1
print('평  문 : ', plainText)
cipherText = encipher(plainText, K)
print('암호문 : ', cipherText)
