import time

naive = lambda a, exp, m: (a ** exp) % m

def modular_exponent(a, exp, m):
    val = a % m
    for i in range(2, exp + 1):
        val = (val * a) % m
    return val


def binary_repr(a, exp, m):
    val, a = 1, a % m
    while exp > 0:
        if exp % 2 == 1:
            val = (val * a) % m
        exp >>= 1
        a *= a % m
    return val

def timer(function, args):
    start = time.time()
    value = function(*args)
    return time.time() - start, value


if __name__ == '__main__':
    values = [4654323, 2456785, 78074741]

    print("{}^{} mod{}".format(*values))

    print("\nModular exponent:\nElapsed: {:.3f}s\nvalue: {}"
          .format(*timer(modular_exponent, values)))

    print("\nBinary representation:\nElapsed: {:.5f}s\nvalue: {}"
          .format(*timer(binary_repr, values)))

