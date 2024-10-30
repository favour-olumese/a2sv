num = int(input())

for _ in range(num):
    n, m = list(map(int, input().split()))
    petya = list(map(int, input().split()))
    vasya= list(map(int, input().split()))

    petya.sort()
    vasya.sort()

    p_l = 0
    p_r = n - 1
    v_l, v_r = 0, m - 1
    total = 0
    while p_l < p_r:
        front_pl = abs(vasya[v_l] - petya[p_l])
        back_pl = abs(vasya[v_r] - petya[p_l])
        front_pr = abs(vasya[v_l] - petya[p_r])
        back_pr = abs(vasya[v_r] - petya[p_r])

        get_max = max(front_pl, back_pl, front_pr, back_pr)
        total += get_max

        if get_max == front_pl:
            p_l += 1
            v_l += 1
        elif get_max == back_pl:
            p_l += 1
            v_r -= 1
        elif get_max == front_pr:
            p_r -= 1
            v_l += 1
        else:
            p_r -= 1
            v_r -= 1

    print(total)