def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_input():
    while True:
        try:
            num = int(input("Enter a prime number: "))
            if is_prime(num):
                return num
            else:
                print(f"{num} is not a prime number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both input numbers must be prime.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Common choice for public exponent (could be dynamic)
    d = pow(e, -1, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    n, e = public_key
    ciphertext = [pow(char, e, n) for char in message.encode()]
    return ciphertext
def decrypt(ciphertext, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message.encode().decode()

# Example usage with user-input primes
p = get_prime_input()
q = get_prime_input()

public_key, private_key = generate_keypair(p, q)

message = input("Enter a message: ")
print(f"Original message: {message}")

encrypted_message = encrypt(message, public_key)
print(f"Encrypted message: {encrypted_message}")
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

decrypted_message = decrypt(encrypted_message, private_key)
print(f"Decrypted message: {decrypted_message}")
