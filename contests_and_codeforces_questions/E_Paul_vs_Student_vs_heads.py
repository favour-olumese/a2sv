a = int(input())
a_list = list(map(int, input().split()))

b = int(input())
b_list = list(map(int, input().split()))

if sum(a_list) != sum(b_list):
    print(-1)
elif len(a_list) == len(b_list):
    print(len(b_list))
else:
    a_set = set(a_list)
    b_set = set(b_list)

    if len(a_set) != len(b_set):
        c = a_set.intersection(b_set)
        print(c)
        print(len(c) + 1)
        
    