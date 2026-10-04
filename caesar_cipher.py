# ==========================================
# CAESAR CIPHER
# Python 3 - Encryption and Decryption
# ==========================================


def caesar_cipher(text, shift, decrypt=False):
    """
    Encrypt or decrypt text using the Caesar Cipher.

    Parameters:
        text (str): The message to process.
        shift (int): Number of positions to shift.
        decrypt (bool): If True, reverse the shift for decryption.

    Returns:
        str: The encrypted or decrypted message.
    """

    # Reverse the shift when decrypting.
    if decrypt:
        shift = -shift

    # Store the processed characters here.
    result = []

    # Process each character in the message.
    for char in text:

        # Handle uppercase letters (A-Z).
        if 'A' <= char <= 'Z':
            base = ord('A')
            shifted_char = chr(
                (ord(char) - base + shift) % 26 + base
            )
            result.append(shifted_char)

        # Handle lowercase letters (a-z).
        elif 'a' <= char <= 'z':
            base = ord('a')
            shifted_char = chr(
                (ord(char) - base + shift) % 26 + base
            )
            result.append(shifted_char)

        # Keep spaces, numbers, and punctuation unchanged.
        else:
            result.append(char)

    # Convert the list of characters back into a string.
    return ''.join(result)


# ==========================================
# TEST THE CAESAR CIPHER
# ==========================================

message = "Hello World"
shift = 3

# Encrypt the message.
encrypted = caesar_cipher(message, shift)

# Decrypt the encrypted message.
decrypted = caesar_cipher(encrypted, shift, decrypt=True)

print("=== CAESAR CIPHER ===")
print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
