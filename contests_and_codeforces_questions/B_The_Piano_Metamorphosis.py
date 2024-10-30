n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
h.insert(0, 0)
mini = float('infinity')
for i in range(1, n):
    h[i] += h[i - 1]

    if i >= 3:
        mini1 = h[i] - h[i - 3]
        if mini1 < mini:
            mini = mini1
            result = i - 3 + 1

print(result)