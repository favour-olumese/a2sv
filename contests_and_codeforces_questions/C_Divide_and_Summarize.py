def pretty(arr, value):
    try:
        if sum(arr) == value:
            return 'Yes'
        mid = (min(arr) + max(arr)) // 2

        if mid > len(arr):
            return 'No'

        if mid == len(arr):
            return 'No'
        
        if len(set(arr)) == 1:
            return 'No'

        left = arr[:mid]
        right = arr[mid:]

        if left == right:
            return 'No'
        

        if value <= sum(left):
            # print(left, value)
            return pretty(left, value)
        else:
            # print(right, value)
            return pretty(right, value)
    except RecursionError:
        return 'No'


n = int(input())


for _ in range(n):
    a_q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(a_q[1]):
        print(pretty(a, int(input())))