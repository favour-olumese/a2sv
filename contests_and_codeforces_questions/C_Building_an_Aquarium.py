test = int(input())

for _ in range(test):
    n_x = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mini = min(nums)
    h = mini + 1
    summ = 0
    print('hello')
    while summ <= n_x[1]:
        print(nums, h)
        temp = list(filter(lambda x: x < h, nums))
        temp1 = list(map(lambda x: h - x, temp))
        summ = sum(temp1)
        h += 1

    print(h - 1)