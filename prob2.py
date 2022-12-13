import random
def exv(x, y):
    s = y[:]
    while len(s) < len(x):
        s += s
    return s[:len(x)]
def alphabet():
    a = ''
    for i in range(65, 91):
        a += chr(i)
    for i in range(10):
        a += str(i)
    for i in range(97, 123):
        a += chr(i)
    return a
def ev(x, y):
    ext_sec = exv(x, y)
    encoded = ''
    aa = alphabet()
    for i in range(len(x)):
        encoded += aa[(aa.index(x[i])+aa.index(ext_sec[i]))%len(aa)]
    return encoded
def dv(x, y):
    ext_sec = exv(x, y)
    decoded = ''
    aa = alphabet()
    for i in range(len(x)):
        decoded += aa[(aa.index(x[i])-aa.index(ext_sec[i]))%len(aa)]
    return decoded
def gs(x, aa):
    y = ''
    for i in range(len(x)):
        ind = random.randint(0, len(aa)-1)
        y += aa[ind]
    return y
def eotp(x):
    y = gs(x, alphabet())
    encoded = ev(x, y)
    return (encoded, y)
def main():
    x = input("Enter the output to be encrypted or decrypted: ")
    encoded, y = eotp(x)
    decoded = dv(encoded, y)
    print('Plain text: ', x)
    print('Cipher: ', y)
    print('ENCODED: ', encoded)
    print('DECODED: ', decoded)
main()