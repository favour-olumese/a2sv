no = int(input())

nums = list(map(int, input().split()))

ng, zr  = 1, 1
l = 0
r = no - 1

neg = []
pos = []
zero = []

while ng > 0:
    ng *= nums[l]
    neg.append(nums[l])
    l += 1

while zr != 0:
    zr *= nums[r]
    zero.append(nums[r])
    r -= 1

pos = nums[l: r + 1]
print(len(neg), ' '.join(list(map(str, neg[::-1]))))
print(len(pos), ' '.join(list(map(str, pos[::-1]))))
print(len(zero), ' '.join(list(map(str, zero[::-1]))))