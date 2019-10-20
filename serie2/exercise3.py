def gcd(a, b):
    '''
    Euclide algorithme
    Same as python's implementation of math.gcd
    '''
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print(gcd(9, 150))
