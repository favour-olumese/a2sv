tests = int(input())

for _ in range(tests):
    x = int(input())
    y = x & -x

    while True:
        # print(x ^ y, x & y, y)
        if x ^ y > 0 and x & y > 0:
            break
        y += 1
    print(y)
    # Got this from Komlanvi Fabrice Eklou and from the tutorial.