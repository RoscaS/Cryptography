
def extended_euclidean(a, b):
    '''
    ax + by = gcd(a, b)
    Solution found on brilliant.org
    :return: (gcd, x, y)
    '''
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        quotient = b // a
        remainder = b % a
        m, n = x - u * quotient, y - v * quotient
        b, a, x, y, u, v = a, remainder, u, v, m, n
    return b, x, y


if __name__ == '__main__':
    a = 1432
    b = 43242
    print(f"{a}x + {b}y = gcd(a, b)")
    print("x: {}\ny: {}\ngcd: {}".format(*extended_euclidean(a, b)))


