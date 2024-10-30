num = list(input())
smallest_num = int(input())

num.sort()

if '0' in num:
    zero_count = num.count('0')
    num = num[zero_count:]
    for _ in range(zero_count):
        num.insert(1, '0')

num = int(''.join(num))

if num == smallest_num:
    print('OK')
else:
    print('WRONG_ANSWER')