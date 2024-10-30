from math import ceil
n, m, a = list(map(int, input().split()))

ans = ceil(m/a) * ceil(n/a)
print(ans)
# Got this from the tutorial for this question.