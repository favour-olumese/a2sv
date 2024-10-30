num = int(input())

res = []
for _ in range(num - 1):
    x, y = list(map(int, input().split()))

    if y in res and x in res:
        x_ind = res.index(x)    
        y_ind = res.index(y)

        if y_ind == 0:
            res.remove(x)
            res.insert(0, x)
        elif y_ind < x_ind:
            res.remove(x)
            res.insert(y_ind, x)
    elif x in res:
        res.append(y)

    elif y in res:
        y_ind = res.index(y)
        res.insert(y_ind, x)
    else:
        res.append(x)
        res.append(y)

print(*res)


