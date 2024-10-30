test = int(input())

for _ in range(test):
    n = int(input())
    bin = list(input())

    zeros = bin.count('0')
    ones = bin.count('1')

    if zeros >= ones:
        print('YES')
    elif zeros > 0:
        print('YES')
    else:
        print('NO')