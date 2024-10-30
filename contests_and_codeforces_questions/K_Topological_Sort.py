from collections import defaultdict, deque

for _ in range(int(input())):
    n, m = list(map(int, input().split()))

    swap = defaultdict(set)

    for _ in range(m):
        a, b = list(map(int, input().split()))
        swap[b].add(a)

    result = [i for i in range(1, n + 1)]

    for i in range(1, n + 1):

        left = i - 2
        while left >= 0 and result[left] in swap[i]:
            # print(left, swap[i], swap)
            # print(result[left], result[left + 1], left, i)
            result[left], result[left + 1] = result[left + 1], result[left]
            left -= 1

    print(*result)
    # Explained by Nahom Amare in A2SV Class.