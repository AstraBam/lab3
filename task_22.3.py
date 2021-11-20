scoring = {1: [8, 2], 2: [6, 9], 3: [42, 56], 20: [50, 3]}


def score(*args):
    global scoring
    if len(args) == 1:
        if args[0] == 'Яблочко':
            return 50
        else:
            return 25
    else:
        if args[0] == 'Внешнее_кольцо':
            return scoring[args[1]][0]
        else:
            return scoring[args[1]][1]


print(score(input()))
