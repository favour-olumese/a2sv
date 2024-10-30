n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

arr = [0 for _ in range(m)]
summ = 0

for num in nums:
    summ += (num % m)
    arr[summ % m] += 1

result = arr[0]

for a in arr:
    result += ((a * (a - 1)) // 2)

print(result)