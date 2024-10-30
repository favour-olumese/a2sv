tests = int(input())

for _ in range(tests):
    num = int(input())
    nums =  list(map(int, input().split()))
    no = False
    minie = max(nums)
    for i in range(1, num):
        # print(i)
        # print(abs(nums[i - 1] - nums[i]))
        minie = min(abs(nums[i - 1] - nums[i]), minie)

    val = max(nums)
    mini = min(nums)
    maxi = max(nums)
    for i in range(mini + 1, maxi):
        if i not in nums:
            val = min(i  - mini, i - maxi)

    if val < minie:
        print('YES')
    else:
        print('NO')