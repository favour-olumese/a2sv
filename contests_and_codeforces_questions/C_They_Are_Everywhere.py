n = int(input())
string = input()
str_set_len = len(set(string))

l = r = 0
result = n
counter = {}
while r < n:
    counter[string[r]] = 1 + counter.get(string[r], 0)
        
    while (len(counter) == str_set_len) and (r - l + 1 >= str_set_len):
        result = min(r - l + 1, result)
        counter[string[l]] = counter.get(string[l], 0) - 1
        if counter.get(string[l]) == 0:
            del counter[string[l]]
        l += 1
        
    r += 1

print(result)