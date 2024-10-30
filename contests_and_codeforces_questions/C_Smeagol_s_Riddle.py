n = int(input())

for i in range(n):
    word = input()
    count = 0

    if word == word[::-1]:
        print(count)
    else:
        l = word[:len(word) // 2]
        r = word[len(word) // 2:]
        r = r[::-1]

        for i in range(len(l)):
            if l[i] != r[i]:
                count += 1
        print(count)