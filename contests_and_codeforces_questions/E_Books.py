num_t = list(map(int, input().split()))
books = list(map(int, input().split()))

books.sort()

time_now = 0
book_count = 0

for time in books:
    time_now += time

    if time_now > num_t[1]:
        break
    
    book_count += 1

print(book_count)