# from collections import deque
no = int(input())

nums = list(map(int, input().split()))
nums1 = []
count = -1
temp = 0
sort_num = sorted(nums)

for i in range(no):
    if nums[i] != sort_num[i]:
        count += 1

print(count)

# Based on David Shalom approach in contest analysis.=-0p

# if sorted(nums) == nums:
#     print(0)
# else:
#     for num in nums:
#         if num < temp:
#             val = num
#             if num not in nums1:
#                 nums1.append(num)
#                 count += 1

#             break

#         if num in nums1:
#             pass
#         else:
#             nums1.append(num)
#             count += 1
    
#             temp = num
#     nums1.sort()
#     idx = nums1.index(val)

#     print(count - idx)