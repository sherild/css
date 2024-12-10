import random

# modular exponentiation (base^exp % mod)
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # If the exponent is odd
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Diffie-Hellman Key Exchange
def diffie_hellman():
    # Step 1: Publicly shared prime number (p) and base (g)
    p = 23  # A small prime number for simplicity
    g = 5  # A primitive root modulo p
    print(f"Publicly Shared Prime (p): {p}")
    print(f"Publicly Shared Base (g): {g}")

    # Step 2: Alice chooses her private key
    a = random.randint(1, p - 1)  # Alice's private key
    print(f"\nAlice's Private Key: {a}")

    # Step 3: Bob chooses his private key
    b = random.randint(1, p - 1)  # Bob's private key
    print(f"Bob's Private Key: {b}")

    # Step 4: Alice and Bob compute their public keys
    A = mod_exp(g, a, p)  # Alice's public key
    B = mod_exp(g, b, p)  # Bob's public key
    print(f"\nAlice's Public Key: {A}")
    print(f"Bob's Public Key: {B}")

    # Step 5: Alice and Bob exchange their public keys and compute the shared secret
    shared_secret_alice = mod_exp(B, a, p)  # Alice computes the shared secret
    shared_secret_bob = mod_exp(A, b, p)  # Bob computes the shared secret
    print(f"\nShared Secret (Alice computes): {shared_secret_alice}")
    print(f"Shared Secret (Bob computes): {shared_secret_bob}")

    # Verify that both shared secrets are the same
    if shared_secret_alice == shared_secret_bob:
        print("\nKey Exchange Successful! Both parties have the same shared secret.")
    else:
        print("\nKey Exchange Failed! Shared secrets do not match.")

# execute Diffie-Hellman Key Exchange
if __name__ == "__main__":
    diffie_hellman()
