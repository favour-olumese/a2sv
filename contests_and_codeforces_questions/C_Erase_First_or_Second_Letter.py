tests = int(input())

def recurse(word, ans):
    if len(word) == 1:
        ans.add(word[-1])
        return
    ans.add(word)

    recurse(word[1:], ans)
    if len(word) >= 2:
        recurse(word[0] + word[2:], ans)

for _ in range(tests):
    length = int(input())
    word = input()
    ans = set()

    recurse(word, ans)
    print(len(ans))