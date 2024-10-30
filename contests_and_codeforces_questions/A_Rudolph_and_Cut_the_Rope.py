test = int(input())

for _ in range(test):
    nails = int(input())

    count = 0
    for _ in range(nails):
        nail, rope = list(map(int, input().split()))

        if nail > rope:
            count += 1

    print(count)