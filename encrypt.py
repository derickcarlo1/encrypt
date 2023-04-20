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
    welcome = pyfiglet.figlet_format("Vigenere Cipher")
    print("\033[1m" + welcome + "\033[0m")
    print("Welcome to my Derick's Vigenere encryption tool! This program will encrypt the message you'll provide")

    # Get the message and keyword from the user
    plaintext = input("\nEnter your message (uppercase letters ONLY and NO spaces): ")
    keyword = input("Enter your keyword (uppercase letters ONLY): ")

    # Encrypt the given message through Vigenere cipher
    ciphertext = vigenere_cipher_encrypt(plaintext, keyword)

    # Show the encrypted message
    print("\nYour encrypted message is:\n")
    print("\033[1m" + pyfiglet.figlet_format(ciphertext) + "\033[0m")

# Ask if the user wants to encrypt another message

# Show a 'goodbye' message