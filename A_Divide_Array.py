n = int(input())

nums = list(map(int, input().split()))

output = 0
stack = []
value = 1
p = 0
n = 0
z = 0
for i in nums:
    value *= 1

    if output == 2:
        value *= i
        stack.append(i)
        if value == 0:
            print(len(stack), ' '.join(list(map(str, stack[::-1]))))
    elif output == 1:
        value *= i
        stack.append(i)
        if value > 0:
            print(len(stack), ' '.join(list(map(str, stack[::-1]))))
            stack.clear()
            value = 1
            output += 1

    else:
        value *= i
        stack.append(i)
        if value < 0:
            print(len(stack), ' '.join(list(map(str, stack[::-1]))))
            stack.clear()
            value = 1
            output += 1