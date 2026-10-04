# ==========================================
# SUBSTITUTION CIPHER
# Python 3 - Encryption and Decryption
# ==========================================


# Standard alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Substitution key.
# Each position in KEY corresponds to the same
# position in ALPHABET.
KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"


def validate_key(key):
    """
    Validate that the substitution key contains
    all 26 letters of the English alphabet exactly once.
    """

    # Convert the key to uppercase so the internal
    # representation is always consistent.
    key = key.upper()

    # A substitution alphabet must contain 26 characters.
    if len(key) != 26:
        raise ValueError(
            "Key must contain exactly 26 letters."
        )

    # The key must contain every letter A-Z exactly once.
    if set(key) != set(ALPHABET):
        raise ValueError(
            "Key must contain every letter A-Z exactly once."
        )

    return key


def substitution_encrypt(text, key):
    """
    Encrypt text using a monoalphabetic substitution cipher.
    Uppercase and lowercase letters are preserved.
    Spaces, numbers, and punctuation remain unchanged.
    """

    key = validate_key(key)
    result = []

    for char in text:

        # Handle uppercase letters
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            result.append(key[index])

        # Handle lowercase letters
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            result.append(key[index].lower())

        # Leave spaces, numbers, and punctuation unchanged
        else:
            result.append(char)

    return ''.join(result)


def substitution_decrypt(text, key):
    """
    Decrypt text using the reverse of the substitution key.
    Uppercase and lowercase letters are preserved.
    Spaces, numbers, and punctuation remain unchanged.
    """

    key = validate_key(key)

    # Build the reverse mapping:
    # substituted letter -> original letter
    reverse = {}

    for i in range(26):
        reverse[key[i]] = ALPHABET[i]

    result = []

    for char in text:

        # Handle uppercase letters
        if 'A' <= char <= 'Z':
            result.append(reverse[char])

        # Handle lowercase letters
        elif 'a' <= char <= 'z':
            result.append(reverse[char.upper()].lower())

        # Leave spaces, numbers, and punctuation unchanged
        else:
            result.append(char)

    return ''.join(result)


# ==========================================
# TEST THE SUBSTITUTION CIPHER
# ==========================================

message = "Hello World"

encrypted = substitution_encrypt(message, KEY)
decrypted = substitution_decrypt(encrypted, KEY)

print("=== SUBSTITUTION CIPHER ===")
print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
