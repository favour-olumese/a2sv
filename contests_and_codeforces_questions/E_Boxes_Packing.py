from collections import Counter
tests = int(input())
nums = list(map(int, input().split()))
count = Counter(nums)
print(max(count.values()))

# Got this concept from Girum Timerga A2SV solution.