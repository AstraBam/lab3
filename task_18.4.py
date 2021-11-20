def check_bracket(str_test):
    stack = []
    for ch in str_test:
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if not stack or stack[-1] != '(':
                print('NO')
                return
            stack.pop()
    if not stack:
        print('YES')
    else:
        print('NO')


dc = {'bracket_check': check_bracket}
s = input()
dc[s[:13]](s[14:-1])

