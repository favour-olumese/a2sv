n = int(input())

for _ in range(n):
    nails = int(input())
    count = 0
    for _ in range(nails):
        nail = list(map(int, input().split()))

        if nail[1] < nail[0]:
            count += 1
        
    print(count)