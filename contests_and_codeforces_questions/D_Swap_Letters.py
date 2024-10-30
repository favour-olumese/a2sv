n = int(input())

for i in range(n):
    m = int(input())
    s = input()
    s_rev = s[::-1]
    count = 0
    t  = 'A'
    while t == 'A':
        t = s_rev[count]
        count += 1

    s = s[:len(s) - count + 1]

    from math import perm
    a = s.count('A')
    b = s.count('B')

    if a == 0 or b == 0:
        print(0)
    else:
        result = perm(m, a) // len(s)
        print(result)