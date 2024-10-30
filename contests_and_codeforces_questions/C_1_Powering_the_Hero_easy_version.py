import heapq
tests = int(input())

for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))
    nums_list = []
    total = 0
    for num in nums:
        if num != 0:
            heapq.heappush(nums_list, -num)
        elif num == 0 and nums_list:
            total -= heapq.heappop(nums_list)
    print(total)