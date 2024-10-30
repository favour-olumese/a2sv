n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
l = r = 0

summ = 0
count = 0
res = 0
while r < n:
    summ += nums[r]
    count += 1
    if summ > m:
        summ -= nums[l]
        l += 1
        count -= 1
    
    res = max(count, res)
    r += 1

print(res)