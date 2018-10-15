def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
   """
    ciphertext=""
    letters=[]
    for i in plaintext:
        letters.append(i)
    for i in range(len(letters)):
        if 'A'<=letters[i]<='W' or 'a'<=letters[i]<='w':
            ciphertext+=chr(ord(letters[i])+3)
        elif 'X'<=letters[i]<='Z' or 'x'<=letters[i]<='z':
            ciphertext+=chr(ord(letters[i])-23)
        elif '!' <= letters[i] <= '@':
            ciphertext += letters[i]
    print(ciphertext)
    return ciphertext
encrypt_caesar(str(input("Введите строку, чтобы ее закодировать:")))

def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    """
    plaintext = ""
    letters = []
    for i in ciphertext:
        letters.append(i)
    for i in range(len(letters)):
        if 'D' <= letters[i] <= 'Z' or 'd' <= letters[i] <= 'z':
            plaintext += chr(ord(letters[i]) - 3)
        elif 'A' <= letters[i] <= 'C' or 'a' <= letters[i] <= 'c':
            plaintext += chr(ord(letters[i]) + 23)
        elif '!'<=letters[i]<='@':
            plaintext +=letters[i]
    print(plaintext)
    return plaintext
decrypt_caesar(str(input("Введите строку, чтобы ее раскодировать:")))
