f = dict()
d = ''
g = []


def setup_profile(name, vacation_dates):
    global f
    global d
    global g
    f = dict()
    d = name
    f[name] = vacation_dates
    g = list(f.keys())


def print_application_for_leave():
    print('Заявление на отпуск в период', f[d], end='. ')
    print(*g)


def print_holiday_money_claim(amount):
    print('Прошу выплатить', amount, 'отпускных денег', end='. ')
    print(*g)


def print_attorney_letter(to_whom):
    print('На время отпуска в период', f[d], 'моим заместителем назначается', to_whom, end='. ')
    print(*g)


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")
