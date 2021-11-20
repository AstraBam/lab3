def golden_ratio(i):
    fib1 = fib2 = 1
    count = 1
    while i != count:
        fib3 = fib1
        fib1 = fib2
        fib2 = fib2 + fib3
        count += 1
    first = fib1
    while i + 1 != count:
        fib3 = fib1
        fib1 = fib2
        fib2 = fib2 + fib3
        count += 1
    second = fib1
    result = second / first
    print(result)

if __name__ == '__main__':
    golden_ratio(int(input()))
