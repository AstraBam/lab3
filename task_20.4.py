def hello(name):
    print('здравствуйте, ', name + '!', ' Вашу карту ищут...')


def search_card(name):
    global base
    if name in base:
        print('ваша карта с номером', base.index(name) + 1, 'найдена')
    else:
        print('Ваша карта не найдена')


if __name__ == '__main__':
    base = ["Иван", "Юлия Иванкова"]
    hello("Иван")
    search_card("Иван")
    hello("Юлия Иванова")
    search_card("Юлия Иванова")
