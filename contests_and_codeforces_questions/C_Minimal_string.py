string = input()
stack = ''
result = ''
count = 0

if string == sorted(string):
    print(string)
else:
    for char in string:
        # Append char in stack that is les than all other chars in string.
        while stack and stack[-1] <= min(string[count:]):
            result += stack[-1]
            stack = stack[:-1]
        stack += char
        count += 1

    # Append the rest of the stack to the result from the top to the bottom.
    if stack:
        result += stack[::-1]
    print(result)