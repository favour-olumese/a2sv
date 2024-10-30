from sys import exit

first = input()
second = input()

if first == second:
    print('YES')
else:
    mid = len(first) // 2
    first1 = first[:mid]
    first2 = first[mid:]
    second1 = second[:mid]
    second2 = second[mid:]

    if first1 == second1 or first1 == second1[::-1]:
        if first2 == second2 or first2 == second2[::-1]:
            print('YES')
            exit()
    if first1 == second2 or first1 == second2[::-1]:
        if first2 == second1 or first2 == second1[::-1]:
            print('YES')
            exit()
    
print('NO')