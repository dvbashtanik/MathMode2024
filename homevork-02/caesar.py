import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if ord(i) in range(65, 91):
            ciphertext += chr((((ord(i)-65)+shift) % 26)+65)
            continue
        if ord(i) in range(97, 123):
            ciphertext += chr((((ord(i)-97)+shift) % 26)+97)
            continue
        ciphertext = ciphertext + i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if ord(i) in range(65, 91):
            plaintext += chr((((ord(i)-65)-shift) % 26)+65)
            continue
        if ord(i) in range(97, 123):
            plaintext += chr((((ord(i)-97)-shift) % 26)+97)
            continue
        plaintext = plaintext + i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
