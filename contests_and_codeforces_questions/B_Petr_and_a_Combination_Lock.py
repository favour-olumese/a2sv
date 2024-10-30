n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

summ = sum(arr)

if summ // 2 in arr:
    print('YES')
elif summ == 0 or summ == 360:
    print('YES')
elif len(set(arr)) == 1 and len(arr) % 2 == 0:
    print('YES')
else:
    print('NO')