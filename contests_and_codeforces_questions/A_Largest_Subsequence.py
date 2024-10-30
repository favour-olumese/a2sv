tests = int(input())

for _ in range(tests):
    num = int(input())
    word = list(input())

    stack = []

    for idx in range(num):
        while stack and word[stack[-1]] <= word[idx]:
            stack.pop()

        stack.append(idx)

    for idx in range(len(stack) // 2):
        word[stack[idx]], word[stack[~idx]] = word[stack[~idx]], word[stack[idx]]

    if word == list(sorted(word)):
        print(len(stack) - 1)
    else:
        print(-1)

