tests = int(input())

for _ in range(tests):
    num = int(input())
    nums = list(map(int, input().split()))

    for i in range(num - 1):
        if nums[i] < min(nums[i + 1:]):
            continue
        for j in range(i + 1, num):
            if nums[i] > nums[j] and nums[i] % 2 == nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

    if sorted(nums) == nums:
        print('YES')
    else:
        print('NO')