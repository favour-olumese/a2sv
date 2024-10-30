n = int(input())

for i in range(n):
    cf = list(input())
    
    codeforces = list('codeforces')
    if cf == codeforces:
        print(0)
    else:
        diff = 0
        for i in range(len(cf)):
            if cf[i] != codeforces[i]:
                diff += 1

        print(diff)