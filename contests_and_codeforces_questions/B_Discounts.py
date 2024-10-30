n = int(input())

costs = list(map(int, input().split()))
costs.sort()
summ = sum(costs)

m = int(input())

q = list(map(int, input().split()))

for amt in q:
    print(summ - costs[-amt])

