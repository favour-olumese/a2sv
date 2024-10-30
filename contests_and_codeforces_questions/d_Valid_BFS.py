from collections import defaultdict, deque
vertices = int(input())

graph = defaultdict(list)

for _ in range(vertices - 1):
    a, b = input().split()

    graph[a].append(b)
    graph[b].append(a)

queue = deque(['1'])
visited = ['1']
while queue:
    node = queue.popleft()
    for neigh in graph[node]:
        if neigh not in visited:
            visited.append(neigh)
            queue.append(neigh)

out = input()
# print(visited)
if ' '.join(visited) == out:
    print('Yes')
else:
    print('No')
    

