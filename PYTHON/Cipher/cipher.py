text = "hi bro how is it going"
custom_key = "Hello"

def vigenere(message, key, direction = 1):
        key_index = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        final_message = ""
        # We loop over each letter in the message (converted to lowercase just in case).
        for char in message.lower() :
            # If the character isn't a letter (like space or punctuation), just add it unchanged.
            if not char.isalpha() :
                final_message += char
            else:
                # Get the corresponding character from the key using the current key index.
                key_char = key[key_index % len(key)]
                # Increment the key index to move to the next character in the key.
                key_index += 1
                # Find the index of the current character in the alphabet.
                offset = alphabet.index(key_char)
                # Find the index of the current character in the alphabet.
                index = alphabet.find(char)
                # Calculate the new index by shifting the current index by the offset.
                # The direction determines whether to encrypt (1) or decrypt (-1).
                new_index = (index + offset * direction) % len(alphabet)
                # Append the character at the new index to the final message.
                final_message += alphabet[new_index]
        # Return the final encrypted or decrypted message.
        return  final_message
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')