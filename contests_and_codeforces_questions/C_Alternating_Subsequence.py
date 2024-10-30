n = int(input())

for i in range(n):
    m = int(input())
    nums = list(map(int, input().split()))

    pos = 0
    neg = -1000000000000
    summ = 0
    for j in range(m):
        if nums[j] > 0:
            if j != 0 and nums[j - 1] < 0:
                summ += neg
                neg = -1000000000000
            pos = max(pos, nums[j])
        if nums[j] < 0:
            if j != 0 and nums[j - 1] > 0:
                summ += pos
                pos = 0
            neg = max(neg, nums[j])
    if nums[-1] > 0:
        summ += pos
    else:
        summ += neg
    
    print(summ)