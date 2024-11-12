# Python program to find HCF (highest common factor) or GCD (greatest common divisor) of two numbers

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


# Using the euclidean algorithm
def hcf_euclidean(x, y):
    while y:
        x, y = y, x % y
    return x
