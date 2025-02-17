from typing import List


def prime(n: int) -> List[int]:
    """Returns all prime numbers up to n using the Sieve of Eratosthenes."""
    if n < 2:
        return []
    primes = [True] * (n + 1)  # Create a boolean array "True" for all numbers
    primes[0], primes[1] = False, False  # 0 and 1 are not prime

    for num in range(2, int(n ** 0.5) + 1):
        if primes[num]:  # If num is still True, it is a prime
            for multiple in range(num * num, n + 1, num):
                primes[multiple] = False  # Mark all multiples of num as False

    return [i for i, is_prime in enumerate(primes) if is_prime]  # Return list of primes


if __name__ == "__main__":
    print(prime(11))
