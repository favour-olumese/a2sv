n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))

    nums.remove(min(nums))

    if sum(nums) >= 10:
        print('YES')
    else:
        print('NO')