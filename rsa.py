import random
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate a random prime number of n bits
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        if is_prime(num):
            return num

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate public and private keys
def generate_keys(bits):
    # Generate two random prime numbers
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    # Compute n (modulus)
    n = p * q

    # Compute phi(n)
    phi_n = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi(n) and e is coprime with phi(n)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Compute d, the modular multiplicative inverse of e (mod phi(n))
    d = pow(e, -1, phi_n)

    # Return public and private keys
    return (e, n), (d, n)

# Function to encrypt a message using the public key
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message using the private key
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Main function
def main():
    # Generate public and private keys
    public_key, private_key = generate_keys(bits=16)

    # Message to be encrypted
    message = "Hello, RSA!"

    # Encrypt the message using the public key
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message using the private key
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
