def find_farthest_orbit(orb):
    sp = []
    index = 0
    for i in orb:
        sp.append(i[0] * i[1])
        index = sp.index(max(sp))
    return orb[index]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
