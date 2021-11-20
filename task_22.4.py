def solve(*coefficients):
    if len(coefficients) == 3:
        d = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
        if coefficients[0] == 0 and coefficients[1] == 0 and coefficients[2] == 0:
            x = ['all']
        elif coefficients[0] == 0 and coefficients[1] == 0:
            x = ''
        elif coefficients[0] == 0:
            x = [-coefficients[2] / coefficients[1]]
        elif coefficients[1] == 0:
            x = [(coefficients[2] / coefficients[0]) ** 0.5]
        elif coefficients[2] == 0:
            x = [0, -coefficients[1] / coefficients[0]]
        else:
            if d == 0:
                x = [-coefficients[1] / (2 * coefficients[0])]
            elif d < 0:
                x = ''
            else:
                x = [float((-coefficients[1] + d ** 0.5) / (2 * coefficients[0])),
                     float((-coefficients[1] - d ** 0.5) / (2 * coefficients[0]))]
        return x
    elif len(coefficients) == 2:
        return [-coefficients[1] / coefficients[0]]
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['all']
        else:
            return []
    else:
        return ['all']


print(sorted(solve(1, 2, 1)))
print(sorted(solve(1, -3, 2)))
