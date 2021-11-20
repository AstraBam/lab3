def line(u, p):
    x = float(p[:p.index(';')])
    y = float(p[p.index(';') + 1:])
    k = float(u[:u.index('x')])
    b = float(u[u.index('x') + 1:])
    print((k * x + b) == y)



dc = {'line': line}
string = input()
pos = string.find(',')
s = string[6:pos - 1]
t = string[pos + 3:-2]
dc[string[:4]](s, t)
