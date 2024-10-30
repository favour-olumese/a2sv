tests = int(input())
 
for _ in range(tests):
    n = int(input())
 
    nums = list(map(int, input().split()))
    nums.sort()
    nums.reverse()
    
    for i in range(n - 1):
        if nums[i] - nums[i + 1] > 1:
            print('NO')
            break
    
    else:
        print('YES')