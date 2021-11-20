def lucky(ticket):
    if sum([int(char) for char in ticket[:3]]) == sum([int(char) for char in ticket[-3:]]):
        print('happy')
    else:
        print('n')


if __name__ == '__main__':
    lucky(input())

