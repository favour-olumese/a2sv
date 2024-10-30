def sum(n):
    if n <= 1:
        return n if n > 0 else 0
    return n  + sum(n - 1)

print(sum(-1))