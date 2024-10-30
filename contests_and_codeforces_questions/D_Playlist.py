n, k = list(map(int, input().split()))

length_list = []
beauty_list = []

for _ in range(n):
    length, beauty = list(map(int, input().split()))
    length_list.append(length)
    beauty_list.append(beauty)

beauty_list_copy = beauty_list[:]
length_list_copy = length_list[:]

total = 0
prev_total = 0
vals = []

for _ in range(k):
    max_beauty = max(beauty_list)
    max_beauty_idx = beauty_list.index(max_beauty)
    beauty_list.pop(max_beauty_idx)
    vals.append(length_list.pop(max_beauty_idx))
    
    total = sum(vals) * max_beauty

    if total > prev_total:
        prev_total = total
    

max_beauty1 = max(beauty_list_copy)
vals1 = []
total1 = 0
prev_total1 = 0

for _ in range(k):
    max_length = max(length_list_copy)
    max_len_idx = length_list_copy.index(max_length)
    vals1.append(length_list_copy.pop(max_len_idx))
    max_beauty1 = min(max_beauty1, beauty_list_copy[max_len_idx])
    total1 = sum(vals1) * max_beauty1

    if total1 > prev_total1:
        prev_total1 = total1


if prev_total > prev_total1:
    print(prev_total)
else:
    print(prev_total1)