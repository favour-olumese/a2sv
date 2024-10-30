from random import shuffle

n = int(input())

for _ in range(n):
    word = input()

    if len(set(word)) == 1:
        print('NO')
    else:
        print('YES')
        word_list = list(word)
        shuffle(word_list)
        result = ''.join(word_list)
        print(result)