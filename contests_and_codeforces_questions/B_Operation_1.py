n = list(map(int, input().split()))

if n[1] > n[0]:
    print(-1)
else:
    temp = n[0] // 2
    if temp % n[1] == 0:
        print(temp)
    else:
        while temp % n[1] != 0:
            temp += 1
        print(temp)