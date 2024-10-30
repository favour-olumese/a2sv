n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
while i < n or j < m:
    if j == m or (i < n and a[i] < b[j]):
        i += 1
    else:
        print(i, end=' ')
        j += 1
