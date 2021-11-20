def partial_sums(*a):
    res = [0]
    for i in range(len(a)):
        res.append(res[i] + a[i])
    return res


print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))
