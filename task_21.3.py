def defractalize(fractal):
    fractal = [a for a in fractal if a is not fractal]
    print(fractal)


if __name__ == '__main__':
    a = [input(), input()]
    a.append(a)
    a.append(input('add: '))
    a.append(a)
    defractalize(a)
