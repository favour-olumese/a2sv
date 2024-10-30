tests = int(input())

for _ in range(tests):
    a, b, l = map(int, input().split())

    power = 1
    k = set()

    while l % (a ** power) == 0:
        power += 1

    power += 1

    for i in range(power, -1, -1):
        a_powered = a ** i

        b_power = 0
        while l % (a_powered * (b ** b_power)) == 0:
            k.add(l // (a_powered * (b ** b_power)))
            b_power += 1

    print(len(k))