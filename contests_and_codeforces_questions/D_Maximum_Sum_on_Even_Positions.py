n = int(input())

for _ in range(n):
    no = int(input())

    nums = list(map(int, input().split()))

    even, odd = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]

    if no % 2 == 1:
        odd += nums[0]
    
    if even > odd:
        print(even)
    else:
        print(odd)