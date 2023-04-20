import pyfiglet

# Define the Vigenere ciper encryption (function)
def vigenere_cipher_encrypt(plaintext, keyword):
    # Translate the keyword into corresponding letter values 0-25
    keyword_values = [ord(c) - ord('A') for c in keyword]

     # Encrypt the plaintext (using Vigenere cipher)
    ciphertext = ""
    i = 0
    for c in plaintext:
        # (Can encrypt uppercase letters ONLY)
        if c.isupper():
            keyword_value = keyword_values[i % len(keyword)]
            ciphertext +=chr(((ord(c) - ord('A') + keyword_value) % 26) + ord('A'))
            i += 1
        else:
            ciphertext += c

    return ciphertext

while True:

# Show a 'welcome' message

# Get the message and keyword from the user

# Encrypt the given message through Vigenere cipher

# Show the encrypted message

# Ask if the user wants to encrypt another message

# Show a 'goodbye' message