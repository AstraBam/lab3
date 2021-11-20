import collections

d = collections.defaultdict(list)
n = int(input())
for _ in range(n):
    e = input().lower()
    d[tuple(sorted(e))].append(e)
v = d.values()
v = filter(lambda w: len(set(w)) > 1, v)
ans = map(lambda x: ' '.join(sorted(x)), v)
print('\n'.join(sorted(ans)))
