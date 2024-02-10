n = int(input())
i = input().split()

total = 0
for num in i:
    total += float(num)

print(f'{total / n:.12f}')