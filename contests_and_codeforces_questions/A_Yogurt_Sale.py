n = int(input())

for _ in range(n):
    num, price_for_one, price_for_two = list(map(int, input().split()))

    tot_price = price_for_one * num
    promo_price = ((num // 2) * price_for_two) + ((num % 2) * price_for_one)

    if promo_price < tot_price:
        print(promo_price)
    else:
        print(tot_price)