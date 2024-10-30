n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))

    summ = a + b

    print(min(a, b, summ // 4))