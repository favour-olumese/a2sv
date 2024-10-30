nums_ops = list(map(int, input().split()))
elements = list(map(int, input().split()))

elements.sort()
result = [0, 0]

if set(elements) == 1:
    print(len(elements), elements[0])
else:
    for i in range(len(elements)):
        count = 0
        add_up = 0
        for j in range(len(elements) - 1, i, -1):
            add_up = elements[i] - elements[j]

            if add_up <= nums_ops[1]:
                count += 1

            elif add_up > nums_ops[1]:
                break

        if count > result[0]:
            result[0], result[1] = count, elements[i]

    print(result[0], result[1])
            
