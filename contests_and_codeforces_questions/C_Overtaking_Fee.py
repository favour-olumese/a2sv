n = int(input())
enter = list(map(int, input().split()))
leave = list(map(int, input().split()))
seen = []
l = 0
e = 0
count = 0
while l < n:
    if enter[e] == leave[l]:
        e += 1
        l += 1
    elif enter[e] in seen:
        e += 1
        
    else:
        seen.append(leave[l])
        l += 1
        count += 1

print(count)