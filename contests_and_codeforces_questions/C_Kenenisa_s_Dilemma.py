n = int(input())
nums = list(map(int, input().split()))
result = []

if sorted(nums) == nums:
    print(0)
else:
    nums1 = nums[:]
    for i in range(n):
        mini = min(nums1)
        if nums[i] > mini:
            result.append(f'{i} {nums.index(mini)}')
            nums[i], nums[nums.index(mini)] = nums[nums.index(mini)], nums[i]
            nums1.remove(mini)
        else:
            nums1.remove(mini)

    print(len(result))
    for num in result:
        print(num)