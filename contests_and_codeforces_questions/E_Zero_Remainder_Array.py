from collections import deque
tests = int(input())

for _ in range(tests):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    to_find = {}

    for num in nums:
        if num % k != 0:
            to_find[-num % k] = 1 + to_find.get(-num % k, 0)

    x = 0
    count = 0
    queue = deque(to_find.items())
    maxi = 0
    while queue:
        rem, count = queue.popleft()

        maxi = max(maxi, rem + 1)

        if count > 1:
            queue.append((rem + k, count - 1))

    
    print(maxi)

    # Explained by Nahom during contest analysis.