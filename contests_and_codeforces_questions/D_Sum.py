num = int(input())

for i in range(num):
    n, k = list(map(int, input().split()))
    nums_list = list(map(int, input().split()))
    total = sum(nums_list)
    nums_list.sort()
    if k == 1:
        maxi = total - sum(nums_list[:2])
        maxi1 = total - nums_list[-1]

        if maxi > maxi1:
            print(maxi)
        else:
            print(maxi1)

    elif k == 2:
        maxi = total - (sum(nums_list[:2]) + nums_list[-1])
        
        print(maxi)