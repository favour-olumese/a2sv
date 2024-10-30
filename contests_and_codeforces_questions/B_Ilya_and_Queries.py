s = input()
n = int(input())

for i in range(n):
    l, r = list(map(int, input().split()))
    l, r = l - 1, r -1
    index = l + 1
    cur_string = s[l]
    result = 0
    while index <= r:

        if s[index] == cur_string:
            index += 1
        else:
            result = max(result, index - l)
            print(index, l)
            l = index
            index += 1
    print(index, l, 'hello')
    result = max(result, index - l - 1)

    print(result)

