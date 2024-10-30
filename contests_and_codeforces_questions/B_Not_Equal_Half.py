from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

not_found = True

if len(set(nums)) == 1:
    print(-1)
else:
    for num in permutations(nums):
        if sum(num[:n]) != sum(num[n:]):
            print(''.join(str(num)[1:-1].split(",")))
            not_found = False
            break

    if not_found:
        print(-1)