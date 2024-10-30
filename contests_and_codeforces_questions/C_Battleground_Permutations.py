import operator
from collections import Counter
from functools import reduce
from math import factorial

n = int(input())

for i in range(n):
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list1 = list(map(int, input().split()))
    num = factorial(len(num_list))
    mults = Counter(num_list).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    print((num // den) * sum(num_list))