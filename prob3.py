def problem3(x):
    a = "abcdefghijklmnopqrstuvwxyz"
    skip = 13
    r = ""
    for i in x:
        find = a.index(i.lower())
        r = r + a[(find+skip)%26]
    return r.upper()
x = input("Enter text to be encrypted: ")
print("Encrypted text: "+problem3(x))

