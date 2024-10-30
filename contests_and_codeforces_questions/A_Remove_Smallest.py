for i in range(int(input())):
    no = int(input())

    nums = list(map(int, input().split()))

    nums.sort()
    found = False
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            print('NO')
            found = True
            break
        
    if not found:
        print('YES')