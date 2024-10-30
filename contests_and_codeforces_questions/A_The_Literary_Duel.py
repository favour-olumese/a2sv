n = int(input())
skills = list(map(int, input().split()))
her = 0
harry = 0
i = 0
while skills:
    if i % 2 == 0:
        if skills[0] > skills[-1]:
            her += skills.pop(0)
        else:
            her += skills.pop()
    else:
        if skills[0] > skills[-1]:
            harry += skills.pop(0)
        else:
            harry += skills.pop()

    i += 1

print(her, harry)