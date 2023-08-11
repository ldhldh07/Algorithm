import sys

si = sys.stdin.readline

N = int(si().strip())

buildings = list(enumerate(map(int, si().strip().split())))

stack = []

'''
(0, 6)
(1, 9)
(1, 9), (2, 5)
(1, 9), (3, 7)
(1, 9), (3, 7), (4, 4)
'''

answer = [0 for _ in range(N)]

for building_index in range(N):
    current_building = buildings[building_index]
    while stack and stack[-1][1] < current_building[1]:
        stack.pop()
    if stack:
        last_higher_building = stack[-1]
        answer[building_index] = last_higher_building[0] + 1
    stack.append(current_building)

print(*answer, sep=" ")