testcases = int(input())

for _ in range(testcases):
    buckets_no = int(input())
    buckets_sum = sum(list(map(int, input().split())))

    root = buckets_sum ** 0.5

    if root.is_integer():
        print('YES')
    else:
        print('NO')