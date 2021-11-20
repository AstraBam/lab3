def ask_password():
    key = 'password'
    count = 0
    for i in range(3):
        scan_str = input()
        if scan_str == key:
            print('Пароль принят')
            break
        else:
            count += 1
            if count == 3:
                print('В доступе отказано')


exec(input())