def solution():
    n = int(input())
 
    passengers = 0
    maximum = 0
    while n > 0:
        l, e = map(int, input().split())
        passengers += e
        passengers -= l
 
        if passengers > maximum:
            maximum = passengers
 
        n -= 1
    print(maximum)
 
 
solution()