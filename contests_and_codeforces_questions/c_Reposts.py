from collections import defaultdict, deque
tests = int(input())

graph = defaultdict(list)

for _ in range(tests):
    reposter, rp, poster = input().split()

    graph[poster.lower()].append(reposter.lower())


# print(graph)

queue = deque()
queue.append(['polycarp', 1])
visited = set('polycarp')
maxi = 1

while queue:
    node, level = queue.popleft()
    maxi = max(level, maxi)
    for neigh in graph[node]:
        if neigh not in visited:
            queue.append([neigh, level + 1])
            visited.add(neigh)

print(maxi)