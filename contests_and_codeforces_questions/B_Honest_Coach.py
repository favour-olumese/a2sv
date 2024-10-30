n = int(input())

for i in range(n):
    num = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    weak = []
    strong = []
    count = 0
    while count < num:
        weak.append(nums[count])
        count += 1

        if count < num:
            strong.append(nums[count])
            count += 1

    print(abs(max(weak) - min(strong)))