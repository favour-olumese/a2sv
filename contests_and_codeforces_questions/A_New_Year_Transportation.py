n, t = list(map(int, input().split()))
cells = list(map(int, input().split()))
i = 1
possible = False
 
while i <= t and i <= n - 1:
    i += cells[i - 1]
    
    if i == t:
        possible = True
        
if possible:
    print('YES')
else:
    print('NO')