n, m = list(map(int, input().split()))


nums = list(map(int, input().split()))

problems = set()
last_problem = float('-inf')
val = ''

for i in nums:
    problems.add(i)

    if len(problems) == n:
        last_problem = i
        problems.add(' ')

    if i == last_problem:
        val += '1'
    else:
        val += '0'

print(val)