n, m = list(map(int, input().split()))
first_arr = list(map(str, input().split()))
second_arr = list(map(str, input().split()))

first_arr.extend(second_arr)
first_arr.sort(key=int)

print(' '.join(first_arr))

'''
while i < a.size() || j < b.size():
    if j == b.size() || i < a.size() && a[i] < b[j]:
       c[i + j] = a[i]
       i++
    else:
       c[i + j] = b[j]
       j++
'''


