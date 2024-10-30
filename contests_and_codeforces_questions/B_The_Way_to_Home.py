dest, jump = list(map(int, input().split()))
path = list(input())
start = 0
count = 0

while start < dest - 1:
    reach = start + jump

    while reach > dest - 1:
        reach -= 1

    if reach <= start:
        print(-1)
        break

    temp, start = start, reach
    while path[start] == '0':
        start -= 1
    
    if start == temp:
        print(-1)
        break
    else:
        count += 1

if start == dest - 1:
    print(count)