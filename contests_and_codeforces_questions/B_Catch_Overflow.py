n = int(input())
res = 0
nums = []
for _ in range(n):
    if res >= 2**32:
        break
    op = input()
    if op == 'add':
        if nums:
            res += nums[-1]
        else:
            res += 1
    elif 'for' in op:
        _for, times = op.split()
        if nums and nums[-1] < 2**32:
            nums.append(nums[-1]*int(times))
        elif nums == []:
            nums.append(int(times))
        else:
            nums.insert(0, 0)
        
    elif op == 'end':
        nums.pop()

if res >= 2**32:
    print('OVERFLOW!!!')
else:
    print(res)