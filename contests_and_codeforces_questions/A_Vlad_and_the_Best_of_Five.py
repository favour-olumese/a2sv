from collections import Counter
tests = int(input())

for _ in range(tests):
    a_b = Counter(input())
    if a_b['A'] > a_b['B']:
        print('A')
    else:
        print('B')