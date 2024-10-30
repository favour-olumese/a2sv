no = int(input())

nums = list(map(int, input().split()))

positive_sum = 0
neg_odd_max = -10001
pos_odd_min = 10000
for num in nums:
    if num >= 0:
        positive_sum += num
        if num % 2 == 1:
            pos_odd_min = min(pos_odd_min, num)
    elif num % 2 == 1:
        neg_odd_max = max(num, neg_odd_max)

if positive_sum % 2 == 1:
    print(positive_sum)
else:
    print(positive_sum - min(pos_odd_min, -neg_odd_max))

# Followed the tutorial guide.