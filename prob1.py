import string
def e(x,y):
    encoded=''
    user=y.lower()
    for i in user: 
        if i in string.ascii_lowercase: 
            ascii=ord(i)+x 
            if ascii>122: 
                encoded+=chr(ascii-122+96)
            else:
                encoded+=chr(ascii) 
        else:
            encoded+=i 
    return encoded
def d(x,cipher):
    y=''
    for i in cipher: 
        if i in string.ascii_lowercase: 
            value=ord(i)-x 
            if value<97: 
                y+=chr(123-(97-value)) 
            else:
                y+=chr(value) 
        else:y+=i
    return y
def menu():
    print('Enter number of preffered action')
    print('[1] Encrypt text: ')
    print('[2] Decrypt text: ')
    print('[3] Quit:')
def main():
    while True:
        menu()
        choice=input()
        if choice=='1':
            y=input('Enter text to encrypt: ')
            x =int(input('Shift: '))
            hidden = e(x,y)
            print('encoded message: {}'.format(hidden))
        elif choice=='2':
            cipher = input('Enter text to decrypt: ')
            x = int(input('Shift: '))
            y = d(x, cipher)
            print('Decrypted message: {}'.format(y))
        elif choice=='3':
            break
        else:
            print('Invalid choice: ')
main()