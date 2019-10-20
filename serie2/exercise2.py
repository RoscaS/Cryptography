import math


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_smaller_than(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


def sieve_eratosthenes(n):
    a = range(2, n + 1)
    b, c = [], a
    while c[0] < math.sqrt(n):
        first = c[0]
        b += [first]
        c = [i for i in c if i % first != 0]
    return b + c


if __name__ == '__main__':
    print(f"\nTerrible way:")
    value = 60
    primes = primes_smaller_than(value)
    print(f"n: {value}\nprimes smaller than n: {primes}\ncount: {len(primes)}")

    print(f"\nEfficient way:")
    value = 345679
    primes = sieve_eratosthenes(value)
    print(f"n: {value}\ncount: {len(primes)}")
