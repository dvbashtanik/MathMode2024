def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    while len(keyword) < len(plaintext):
        keyword += keyword
    if len(keyword) < len(plaintext):
        keyword = keyword[:len(plaintext) - len(keyword)]
    a = {i-65: chr(i) for i in range(65, 91)}
    b = {i-97: chr(i) for i in range(97, 123)}
    for i in range(len(plaintext)):
        if plaintext[i] in a.values():
            ciphertext += a[(ord(plaintext[i]) + ord(keyword[i]) - 130) % 26]
            continue
        if plaintext[i] in b.values():
            ciphertext += b[(ord(plaintext[i]) + ord(keyword[i]) - 194) % 26]
            continue
        ciphertext = ciphertext + plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    while len(keyword) < len(ciphertext):
        keyword += keyword
    if len(keyword) < len(ciphertext):
        keyword = keyword[:len(ciphertext) - len(keyword)]
    plaintext = ""
    a = {i - 65: chr(i) for i in range(65, 91)}
    b = {i - 97: chr(i) for i in range(97, 123)}
    for i in range(len(ciphertext)):
        if ciphertext[i] in a.values():
            plaintext += a[((ord(ciphertext[i])-65) - (ord(keyword[i])-65) + 26) % 26]
            continue
        if ciphertext[i] in b.values():
            plaintext += b[((ord(ciphertext[i])-97) - (ord(keyword[i])-97) + 26) % 26]
            continue
        plaintext = plaintext + ciphertext[i]
    return plaintext