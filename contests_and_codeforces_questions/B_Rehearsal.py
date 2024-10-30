# testcases = int(input())

# arr = []

# for _ in range(testcases):
#     x_y = list(map(int, input().split()))

#     arr.extend([x_y[1]] * x_y[0])

# arr.sort()

# joint_skill = 10000000000

# for i in range(len(arr) // 2):
#     joint_skill = min(joint_skill, arr[i] + arr[-(i + 1)])


# print(joint_skill)


testcases = int(input())

arr = []

for _ in range(testcases):
    x, y = list(map(int, input().split()))

    arr.append([x, y])

arr.sort(key=lambda w: w[1])

left, right = 0, len(arr) - 1

min_time = float('-inf')

while left <= right:
    min_time = max(min_time, arr[left][1] + arr[right][1])
    diff = min(arr[left][0], arr[right][0])

    # This would cater for arrays with whose len has an odd index
    # When the left == right, we divide its occurrences which would 
    # be removed twice from the arr.
    if left == right:
        diff //= 2

    arr[left][0] -= diff
    arr[right][0] -= diff

    if arr[left][0] == 0:
        left += 1
    if arr[right][0] == 0:
        right -= 1

print(min_time)

# Code by Komlanvi Fabrice Eklou
