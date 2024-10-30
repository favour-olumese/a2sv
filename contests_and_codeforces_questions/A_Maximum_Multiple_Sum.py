for _ in range(int(input())):
    num = int(input())
    maxi = 2
    prev_total = 0
    d = 2
    while d <= num:
        total = sum(range(d, num + 1, d))
        if total > prev_total:
            prev_total = total
            maxi = d

        d += 1

    
    print(maxi)