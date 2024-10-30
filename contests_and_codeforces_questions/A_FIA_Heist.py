word = input()

stack = []
backspace = ['<', '-']

for char in word:
    if stack:
        if char == '<':
            stack.pop()

    if char not in backspace:
        stack.append(char)

print(''.join(stack))