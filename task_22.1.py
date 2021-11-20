small = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
tall = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encrypt_caesar(msg, shift):
    mes = ""
    for x in msg:
        if x in small:
            ind = small.index(x)
            mes += small[ind + shift]
        elif x in tall:
            ind = tall.index(x)
            mes += tall[ind + shift]
        else:
            mes += x
    print(mes)


def decrypt_caesar(msg, shift):
    mes = ""
    for x in msg:
        if x in small:
            ind = small.index(x)
            mes += small[ind - shift]
        elif x in tall:
            ind = tall.index(x)
            mes += tall[ind - shift]
        else:
            mes += x
    print(mes)


if __name__ == '__main__':
    a = int(input('dec - 1 or enc - 2\n'))
    if a == 2:
        encrypt_caesar(input(), int(input('сдвиг - ')))
    elif a == 1:
        decrypt_caesar(input(), int(input('сдвиг - ')))
