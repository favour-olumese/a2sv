n = int(input())

for _ in range(n):
    mins = int(input())
    s = input()

    s_set = set(s)
    result = 0
    for char in s_set:

        count = s.count(char)
        char_num = ord(char) - 64

        if count >= char_num:
            result += 1

    print(result)