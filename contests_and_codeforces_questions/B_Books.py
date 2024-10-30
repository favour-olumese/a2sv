n, t = list(map(int, input().split()))
mins = list(map(int, input().split()))

l = r = 0
summ = 0
count = 0
result = 0

while r < n:
    summ += mins[r]
    count += 1
    if summ > t:
        summ -= mins[l]
        l += 1
        count -= 1

    result = max(result, count)
    r += 1

print(result)    