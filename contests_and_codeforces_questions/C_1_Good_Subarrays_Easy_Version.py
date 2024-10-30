t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, (input().split())))

  left = 0
  i = 1
  pairs_count = 0

  for right in range(n):
    while a[right] < i:
      left += 1
      i -= 1
    
    pairs_count += right - left + 1
    i += 1
  print(pairs_count)