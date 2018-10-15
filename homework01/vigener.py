def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    d = {}
    v=0 # v - value
    for i in range(ord('A'), ord('Z')):
        d[chr(i)] = v
        v+=1
    d_small = {}
    v=0
    for i in range(ord('a'), ord('z')):
        d_small[chr(i)] = v
        v+=1
    ciphertext = ""
    keyword *= len(plaintext) // len(keyword) + 1
    key = []
    letters = []
    for i in keyword:
        if 'A'<=i<='Z':
            key.append(d[i])
        else:
            key.append(d_small[i])
    for i in plaintext:
        if 'A'<=i<='Z':
            letters.append(d[i])
        else:
            letters.append(d_small[i])
    for i in range(len(letters)):
        s = (letters[i]+key[i]) % 26
        if 'A'<=plaintext[1]<='Z':
            for k, v in d.items():  # k-key; v-value
                if s == v:
                    ciphertext += k
        else:
            for k, v in d_small.items():  # k-key; v-value
                if s == v:
                    ciphertext += k
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
    d = {}
    v=0 # v - value
    for i in range(ord('A'), ord('Z')):
        d[chr(i)] = v
        v+=1
    d_small = {}
    v=0
    for i in range(ord('a'), ord('z')):
        d_small[chr(i)] = v
        v+=1
    plaintext = ""
    keyword *= len(ciphertext) // len(keyword) + 1
    key = []
    letters = []
    for i in keyword:
        if 'A'<=i<='Z':
            key.append(d[i])
        else:
            key.append(d_small[i])
    for i in ciphertext:
        if 'A'<=i<='Z':
            letters.append(d[i])
        else:
            letters.append(d_small[i])
    for i in range(len(letters)):
        s = (letters[i]-key[i]+26) % 26
        if 'A'<=ciphertext[1]<='Z':
            for k, v in d.items():  # k-key; v-value
                if s == v:
                    plaintext += k
        else:
            for k, v in d_small.items():
                if s == v:
                    plaintext += k
    print(plaintext)
    return plaintext

ciphertext = str(input("Введите строку, чтобы ее раскодировать: "))
keyword = str(input("Введите кодовое слово: "))
decrypt_vigenere(ciphertext,keyword)
