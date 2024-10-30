n = int(input())

for _ in range(n):

    letters = list(input())
    if sorted(letters) == letters:
        print('YES')
    elif sorted(letters) == letters[::-1]:
        print('YES')
    else:
        count = 0
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                if letters[i] > letters[j]:
                    letters[i], letters[j] = letters[j], letters[i]

                    count += 1

            if count > 1:
                print('NO')
                break

        if count <= 1:
            print('YES')

                
                

            