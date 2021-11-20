def palindrome(s):
    s = s.replace(' ', '')
    s = s.lower()
    if s == s[::-1]:
        print('y')
    else:
        print('n')


palindrome(input())
