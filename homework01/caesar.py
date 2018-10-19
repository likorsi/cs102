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
    for i in plaintext:
        if 'A'<=i<='W' or 'a'<=i<='w':
            ciphertext+=chr(ord(i)+3)
        elif 'X'<=i<='Z' or 'x'<=i<='z':
            ciphertext+=chr(ord(i)-23)
        elif '!' <= i <= '@':
            ciphertext += i
    print(ciphertext)
    return ciphertext

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
    for i in ciphertext:
        if 'D' <= i <= 'Z' or 'd' <= i <= 'z':
            plaintext += chr(ord(i) - 3)
        elif 'A' <= i <= 'C' or 'a' <= i <= 'c':
            plaintext += chr(ord(i) + 23)
        elif '!'<= i <='@':
            plaintext += i
    print(plaintext)
    return plaintext
