n = int(input())
nums = list(map(int, input().split()))
stack = []

sq = 0
maxi_len = 0

for num in nums:
    if stack:
        if stack[-1] != num:
            temp = sq
            sq = max(sq, num * len(stack))
            if temp != sq:
                maxi_len = stack[-1]
            stack.clear()

    stack.append(num)

temp = sq
sq = max(sq, num * len(stack))
if temp != sq:
    maxi_len = stack[-1]
print(maxi_len)
