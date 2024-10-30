from collections import deque

tests = int(input())

for _ in range(tests):
    no = int(input())
    nums = list(map(int, input().split()))
    nums_map = {k:v for v, k in enumerate(nums)}
    nums.sort()
    nums_prefix = deque([0])
    result = [0] * no

    for num in nums:
        nums_prefix.append(num + nums_prefix[-1])
        # nums_prefix = nums_prefix[1:]
    idx = no - 1
    for i in range(no - 2, -1 , -1):
        if nums_prefix[i] < nums[i]:
            idx = nums_map[i]
        result[i] = idx

    print(*result)

    