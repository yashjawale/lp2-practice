import math

# Function to encrypt a message using a transposition cipher
def encrypt(message, key):
    num_columns = len(key)
    num_rows = int(math.ceil(len(message) / num_columns))
    padded_message = message + (' ' * (num_rows * num_columns - len(message)))
    
    ciphertext = [''] * num_columns
    
    for column in range(num_columns):
        for row in range(num_rows):
            index = row * num_columns + key[column] - 1
            ciphertext[column] += padded_message[index]
    
    return ''.join(ciphertext)

# Function to decrypt a message using a transposition cipher
def decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = int(math.ceil(len(ciphertext) / num_columns))
    
    reordered_ciphertext = [''] * len(ciphertext)
    for i, k in enumerate(key):
        reordered_ciphertext[num_rows * (k - 1): num_rows * k] = ciphertext[i * num_rows: (i + 1) * num_rows]
    
    plaintext = [''] * num_rows
    
    for row in range(num_rows):
        for column in range(num_columns):
            index = column * num_rows + row
            plaintext[row] += reordered_ciphertext[index]
    
    return ''.join(plaintext).rstrip()

# Main function
def main():
    key = [3, 1, 4, 2]
    message = "Hello world"
    
    encrypted_message = encrypt(message, key)
    print("Encrypted Message:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
