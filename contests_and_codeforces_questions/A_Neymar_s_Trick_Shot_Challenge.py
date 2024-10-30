x, n = list(map(int, input().split()))
l = list(map(int, input().split()))

res = 1
summ = 0

for s in l:
    summ += s
    if summ <= n:
        res += 1
    elif summ > n:
        break
print(res)