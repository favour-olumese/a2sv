from collections import deque
exp = int(input())
time = deque()

for _ in range(exp):
    start, end, rooms = list(map(int, input().split()))

    time.append((start, rooms))
    time.append((end + 1, -rooms))

time = deque(sorted(time))
# print(time)

max_room = 0
rms = 0

for tm, rm in time:
    rms += rm
    max_room = max(max_room, rms)

print(max_room)