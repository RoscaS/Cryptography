import math


def euler_totient(value):
    if value < 1:
        return "/"
    return sum([1 for i in range(1, value + 1) if math.gcd(value, i) == 1])


if __name__ == '__main__':
    value = 52
    print(f'φ({value}) = {euler_totient(value)}')
