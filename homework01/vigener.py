def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword *= len(plaintext) // len(keyword) + 1
    for i in range(len(plaintext)):
        key = ord(keyword[i])
        if 'A' <= plaintext[i] <= 'Z':
            key -= ord('A')
        else:
            key -= ord('a')
        sum = chr(ord(plaintext[i])+key)
        if 'A' <= sum <= 'Z' or 'a' <= sum <= 'z':
            ciphertext += sum
        else:
            ciphertext += chr(ord(sum)-26)
    print(ciphertext)
    return ciphertext

plaintext = str(input("Введите строку, чтобы ее закодировать: "))
keyword = str(input("Введите кодовое слово: "))
encrypt_vigenere(plaintext,keyword)


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword *= len(ciphertext) // len(keyword) + 1
    for i in range(len(ciphertext)):
        key = ord(keyword[i])
        if 'A' <= ciphertext[i] <= 'Z':
            key -= ord('A')
        else:
            key -= ord('a')
        sum = chr(ord(ciphertext[i]) + key)
        if 'A' <= sum <= 'Z' or 'a' <= sum <= 'z':
            plaintext += sum
        else:
            plaintext += chr(ord(sum) - 26)
    print(plaintext)
    return plaintext

ciphertext = str(input("Введите строку, чтобы ее раскодировать: "))
keyword = str(input("Введите кодовое слово: "))
decrypt_vigenere(ciphertext,keyword)