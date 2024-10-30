def prime_factor(num):
    d = 2
    prime = set()
    while d * d <= num:
        while num % d == 0:
            prime.add(d)
            num //= d    
        d += 1

    if num > 1:
        prime.add(num)

    return len(prime)

n = int(input())

ans = 0

for i in range(n + 1):
    if prime_factor(i) == 2:
        ans += 1

print(ans)