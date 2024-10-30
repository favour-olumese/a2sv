n = int(input())

for _ in range(n):
    m, n = list(map(int, input().split()))
    mini = min(m, n)

    m_plus_n = m + n

    div_4 = m_plus_n // 4

    result = min(div_4, mini)

    print(result)