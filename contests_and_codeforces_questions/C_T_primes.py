tests = int(input())

nums = list(map(int, input().split()))

maxi = 1000001

is_prime = [True for _ in range(maxi)]
is_prime[0] = is_prime[1] = False

d = 2
prime = set()
while d * d <= maxi:
    if is_prime[d]:
        j = d * d
        prime.add(j)
        while j < maxi:
            is_prime[j] = False
            j += 1
    d += 1

for num in nums:
    if num in prime:
        print('YES')
    else:
        print('NO')