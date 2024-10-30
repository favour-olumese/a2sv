n = int(input())

stack = []
count = 0
l = 1
for _ in range(2 * n):
    command = input()
    if command != 'remove':
        stack.append(int(command[4:]))
    else:
        if stack and stack[-1] != l:
            stack.clear()
            count += 1
        if stack:
            stack.pop()
        
        l += 1

print(count)