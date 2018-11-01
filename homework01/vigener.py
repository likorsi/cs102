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
        sum = (ord(plaintext[i]) + key)
        if sum > ord('Z') and 'A' <= plaintext[i] <= 'Z':
            sum -= 26
        elif sum > ord('z') and 'a' <= plaintext[i] <= 'z':
            sum -= 26
        ciphertext += chr(sum)
    print(ciphertext)
    return ciphertext


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
        sum = (ord(ciphertext[i]) - key)
        if sum < ord('A') and 'A' <= ciphertext[i] <= 'Z':
            sum += 26
        elif sum < ord('a') and 'a' <= ciphertext[i] <= 'z':
            sum += 26
        plaintext += chr(sum)
    print(plaintext)
    return plaintext
