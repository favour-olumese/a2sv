n, k, q = list(map(int, input().split()))

temps = {}
for _ in range(n):
    l, r = list(map(int, input().split()))
    for temp in range(l, r + 1):
        temps[temp] = 1 + temps.get(temp, 0)

for _ in range(q):
    a, b = list(map(int, input().split()))
    count = 0
    for temp in range(a, b + 1):
        if temp in temps and temps[temp] >= k:
            count += 1
    print(count)