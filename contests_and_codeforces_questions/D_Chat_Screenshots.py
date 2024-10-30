from collections import defaultdict, deque
tests = int(input())

for _ in range(tests):
    n, k = list(map(int, input().split()))

    graph = defaultdict(list)
    in_degree = {k:0 for k in range(1, n + 1)}

    for _ in range(k):
        nums = list(map(int, input().split()))
        for i in range(1, n - 1):
            graph[nums[i]].append(nums[i+1])
            in_degree[nums[i+1]] += 1

    bfs = deque([num for num in range(1, n + 1) if in_degree[num] == 0])

    visited = []
    while bfs:
        node=bfs.popleft()
        visited.append(node)

        for neigh in graph[node]:
            in_degree[neigh] -= 1

            if in_degree[neigh] == 0:
                bfs.append(neigh)

    if len(visited) == n:
        print('YES')
    else:
        print('NO')
    
    # Explained by Abel Gebeyehu A2SV during contest analysis.