n = int(input())

for _ in range(n):
    k_q = input()
    k = list(map(int, input().split()))
    q = list(map(int, input().split()))

    for e in q:
        value = e
        k_copy = k.copy()
        if value >= k[0]:
            while k_copy:
                if value >= k_copy[-1]:
                    value -= len(k_copy)
                else:
                    k_copy.pop()

        print(value, end=' ')
    print()