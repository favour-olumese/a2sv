tests = int(input())

cat = ['m', 'e', 'o', 'w']

for _ in range(tests):
    no = int(input())
    chars = input()
    i = 0
    yes = True
    for char in chars:
        if i < 4 and char.lower() == cat[i]:
            i += 1
        if i == 4 and char.lower() != 'w':
            print('NO')
            yes = False
            break

    if yes and i == 4:
        print('YES')
    elif yes and i < 4:
        print('NO')
        
