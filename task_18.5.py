def equation(a, b):
    x1, y1, x2, y2 = map(float, (a + ";" + b).replace(',', '.').split(';'))
    if x1 == x2:
        print('prover x. ', x1)
    else:
        if y1 == y2:
            print('prover y. ', y1)
        else:
            k = (y2 - y1) / (x2 - x1)
            print(k, y2 - k * x2)



equation("0;0", "1;1")
equation("0;0", "0;4")
equation((input()), (input()))
