list = []
while True:
    try:
        words = str(input())
        if words == '':
            break
        list.append(words)
    except Exception as e:
        break

print(*sorted(list, key=lambda word: sum([(ord(i) - ord('A') + 1) for i in word.upper()])), sep='\n')
