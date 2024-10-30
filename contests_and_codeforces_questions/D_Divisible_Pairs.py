num = int(input())

for _ in range(num):
    n, x, y = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] + nums[j]) % x == 0 and (nums[i] - nums[j]) % y == 0:count += 1

    print(count)