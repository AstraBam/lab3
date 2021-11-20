def print_only_new(message):
    if message not in old:
        print(message)


if __name__ == '__main__':
    old = set()
    while True:
        message = input()
        if message == 's':
            break
        print_only_new(message)
        old.add(message)
