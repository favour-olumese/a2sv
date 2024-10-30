n = int(input())

for i in range(n):
    num = input()
    nums = list(map(int, input().split()))
    nums_copy = nums.copy()
    location = []
    total = 0
    i = 1
    for i in range(3):
        location.append(nums_copy.index(max(nums_copy)) + i)
        total += max(nums_copy)
        nums_copy.remove(max(nums_copy))
        i += 1

    total += min(location) - max(location)
    print(total)