# Function to encrypt or decrypt a message using XOR
def xor_cipher(message, key):
    # Convert message and key to bytes
    message_bytes = message.encode()
    key_bytes = key.encode()
    
    # Perform XOR operation on each byte of the message with the corresponding byte of the key
    result = bytearray()
    for i in range(len(message_bytes)):
        result.append(message_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    # Convert the result back to a string
    return result.decode()

# Main function
def main():
    # Example message and key
    message = "This is a new type of message"
    key = "abc"
    
    # Encrypt the message
    encrypted_message = xor_cipher(message, key)
    print("Encrypted Message:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = xor_cipher(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
