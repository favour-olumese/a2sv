num = input()

false = False

if num.startswith('1') and len(set(num)) == 1:
    print('YES')

elif not num.startswith('1'):
    print('NO')
else:
    num_list = num.split('1')
    
    acceptable = ['4', '44', '']
    for no in num_list:
        if no not in acceptable:
            print('NO')
            false = True
            break
    if not false:
        print('YES')