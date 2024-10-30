import heapq
n = int(input())
portions = list(map(int, input().split()))

energy = 0
count = 0
negatives = []


for portion in portions:
    # Add negative numbers to a list.
    if portion < 0:
        heapq.heappush(negatives, portion)

    energy += portion
    count += 1

    # Add back previous max negative number if energy goes below 0.
    if energy < 0:
        energy += -heapq.heappop(negatives)
        count -= 1

print(count)

# Concept explained by Fabrice in contest analysis.