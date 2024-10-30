from math import prod
n = int(input())


for _ in range(n):
    num = int(input())
    nums = list(map(int, input().split()))
    mul = prod(nums)
    exp = 2 ** num

    if mul % exp == 0:
        print(0)
    else:
        for i in range(2, len(n) - 1)
    

