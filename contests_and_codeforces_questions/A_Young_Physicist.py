n = int(input())

x = y = z = 0
for _ in range(n):
    coordinates = list(map(int, input().split()))
    x += coordinates[0]
    y += coordinates[1]
    z += coordinates[2]
    
if x == y == z == 0:
    print('YES')
else:
    print('NO')