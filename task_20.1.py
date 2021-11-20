translatedText = ''


def translate(text):
    global translatedText
    dont = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я',
            'А', 'И', 'Е', 'Ё', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', ',', '.', '-']
    for i in range(len(text) - 1):
        if dont.count(text[i]) == 0:
            translatedText = translatedText + text[i]
    translatedText = ' '.join(translatedText.split())
    print(translatedText)


if __name__ == '__main__':
    translate(input())
