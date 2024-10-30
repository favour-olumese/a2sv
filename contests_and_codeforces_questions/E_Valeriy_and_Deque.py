n_q = list(map(int, input().split()))
nums = list(map(int, input().split()))

queries = []

if n_q[1] == 0:
    print()

else:
    for _ in range(n_q[1]):
        num = int(input())
        queries.append(num)

    maxi = max(queries)

    for i in range(1, maxi + 1):
        if nums[1] > nums[0]:
            nums.insert(0, nums.pop(1))
            nums.append(nums.pop(1))
            if i in queries:
                print(nums[-1], nums[0])
        elif nums[0] > nums[1]:
            nums.append(nums.pop(1))
            if i in queries:
                print(nums[0], nums[-1])