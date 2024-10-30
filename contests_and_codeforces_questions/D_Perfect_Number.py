k = int(input())

val = 19
count = 0

while True:
    summ = sum(map(int, list(str(val))))

    if summ == 10:
        count += 1

        if count == k:
            print(val)
            break    
    val += 1

    # Analyzed in Contest anaylysis