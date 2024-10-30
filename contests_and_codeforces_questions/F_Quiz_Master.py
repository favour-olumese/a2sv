tests = int(input())

for _ in range(tests):
    n, m = map(int, input().split())

    skills = list(map(int, input().split()))
    skills.sort()
    val = {}
    for i in range(2, m + 1):
        for skill in skills:
            if skill % i == 0:
                val[i] = skill
    if len(val) == m - 1:
        all_val = list(val.values())
        print(max(all_val) - min(all_val))
    else:
        print(-1)