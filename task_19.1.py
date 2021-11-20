def month_name(num, lang):
    ru = {1: 'январь', 2: "февраль", 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',
          8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
    en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'jule',
          8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
    if lang == 'en':
        print(en[num])
    elif lang == 'ru':
        print(ru[num])


if __name__ == '__main__':
    month_name(int(input()), input())
