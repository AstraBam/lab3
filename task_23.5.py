def same_by(characteristic, objects):
    if not objects:
        return True
    etalon = characteristic(objects[0])
    for obj in objects:
        if characteristic(obj) != etalon:
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
