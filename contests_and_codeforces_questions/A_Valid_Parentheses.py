from collections import deque
s = input()

stack = deque()
count = 0

for char in s:
    if char == '(':
        stack.append('(')
    elif char == ')':
        if stack:
            stack.pop()
            count += 2

print(count)