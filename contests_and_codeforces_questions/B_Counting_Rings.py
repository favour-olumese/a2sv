n = input()

count = 0
count_list = []

if "O" not in n:
    print(count)

else:
    import re
    obj = re.findall('O*O', n)
    maxi = len(max(obj))
    print(maxi)