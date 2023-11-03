import sys
from collections import deque

class Node:
    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

def bfs(start_point, array, r, c, rains):
    queue = deque([start_point])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    rain_queue = deque(rains)

    while queue:
        for _ in range(len(rain_queue)):
            rain_node = rain_queue.popleft()
            for delta_i, delta_j in delta:
                next_rain_i, next_rain_j = rain_node.x + delta_i, rain_node.y + delta_j
                if 0 <= next_rain_i < r and 0 <= next_rain_j < c and array[next_rain_i][next_rain_j] == '.':
                    array[next_rain_i][next_rain_j] = '*'
                    rain_queue.append(Node(next_rain_i, next_rain_j))

        for _ in range(len(queue)):
            current_node = queue.popleft()
            if array[current_node.x][current_node.y] == 'H':
                return current_node.distance
            
            for delta_i, delta_j in delta:
                next_x, next_y = current_node.x + delta_i, current_node.y + delta_j
                if 0 <= next_x < r and 0 <= next_y < c and not visited[next_x][next_y]:
                    if array[next_x][next_y] == '.':
                        visited[next_x][next_y] = 1
                        queue.append(Node(next_x, next_y, current_node.distance + 1))
                    elif array[next_x][next_y] == 'H':
                        return current_node.distance + 1

    return "FAIL"


si = sys.stdin.readline
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

R, C = map(int, si().split())

array = [list(si().strip()) for _ in range(R)]
rains = []

for i in range(R):
    for j in range(C):
        if array[i][j] == 'W':
            start_point = Node(i, j)
        elif array[i][j] == '*':
            rains.append(Node(i, j))

shortest_distance = bfs(start_point, array, R, C, rains)
print(shortest_distance)