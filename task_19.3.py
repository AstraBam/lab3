def roots_of_quadratic_equation(a, b, c):
    mas = []
    d = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        mas.append('all')
        return mas
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        mas.append((-c) / b)
    else:
        if d > 0:
            mas.append((-b + d ** 0.5) / (2 * a))
            mas.append((-b - d ** 0.5) / (2 * a))
        elif d == 0:
            mas.append((-b) / (2 * a))
        elif d < 0:
            return []
        return mas


res = roots_of_quadratic_equation(int(input('a= ')), int(input('b= ')), int(input('c= ')))
if 'all' in res:
    if res == ['all']:
        print('0 0 0')
    else:
        print('err')
else:
    print(*sorted(res))
