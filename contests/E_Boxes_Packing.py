n = int(input())
i = list(map(int, input().split()))

total = 0
count = len(i)
while count > 1:
    for num in i:
        maxi = max(i)
        if num < maxi:
            total += 1
            i.remove(num)
            i.remove(maxi)
        print(i)

print(total)
