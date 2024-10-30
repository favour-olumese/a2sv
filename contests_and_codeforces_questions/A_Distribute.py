from collections import defaultdict
num = int(input())
nums = list(map(int, input().split()))
div = sum(nums) // (num // 2)
# print(div)

nums_dicts = defaultdict(list)

for ind, val in enumerate(nums):
    nums_dicts[val].append(ind + 1)

for i in range(num // 2):
    first = nums_dicts[nums[0]].pop()
    rem = div - nums[0]
    second = nums_dicts[rem].pop()
    print(first, second)

    nums.remove(nums[0])
    nums.remove(rem)