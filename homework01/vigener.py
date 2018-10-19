def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    d = {} #  словарь (d-dictionary) для заглавных букв алфавита
    v=0 # v - value, номер буквы в алфавите
    #  заполним ключи и значения словаря буквами и их номером в алфавите соответственно:
    for i in range(ord('A'), ord('Z')):
        d[chr(i)] = v
        v+=1
    d_small = {} #  словарь для строчных букв алфавита
    v=0
    #  ананлогичное заполнение словаря, но строчными буквами:
    for i in range(ord('a'), ord('z')):
        d_small[chr(i)] = v
        v+=1
    ciphertext = ""
    #  продублируем ключ, пока его длина не превысит шифруемое слово:
    keyword *= len(plaintext) // len(keyword) + 1
    key = [] # список для номера в алфавите букв ключа
    letters = [] #  список для номера в алфавите букв шифруемого слова
    #  присвоим элементам порядковый номер буквы в алфавите с помощью ключа словаря:
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
    #  найдем верную букву по ключу словаря и добавим ее в зашифрованное слово:
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
    #  значения словарей и списков и действия с ними аналогичны функции encrypt_vigenere
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
    #  найдем верную букву по ключу словаря и добавим ее в расшифрованное слово:
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
    return plaintext
