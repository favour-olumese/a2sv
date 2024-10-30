n = int(input())

a = input()
b = input()

graph = [[] for _ in range(26)]

for i in range(n):
    if a[i] != b[i]:
        graph[ord(a[i]) - ord("a")].append(ord(b[i]) - ord("a"))
        graph[ord(b[i]) - ord("a")].append(ord(a[i]) - ord("a"))

visited = [True] * 26
answer = []

for i in range(26):
    if visited[i]:
        stack = [i]

        visited[i] = False

        while stack:
            char = stack.pop()

            for charx in graph[char]:
                visited[charx] = False
                stack.append(charx)
                answer.append((char, charx))


print(len(answer))

for a, b in answer:
    print(chr(a + ord("a")), chr(b + ord("a")))