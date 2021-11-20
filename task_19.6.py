import math


def catalan(n):
    return int((math.factorial(2 * n)) // (math.factorial(n) * math.factorial(n + 1)))


print(catalan(1))
