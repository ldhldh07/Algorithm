from collections import deque

def bfs_union(n, start_i, start_j, l, r, visited):
    queue = deque([(start_i, start_j)])
    union = [(start_i, start_j)]
    visited[start_i][start_j] = 1
    union_sum = world_map[start_i][start_j]
    union_count = 1
    is_moving = False

    while queue:
        current_i, current_j = queue.popleft()

        for delta_i, delta_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_i, next_j = current_i + delta_i, current_j + delta_j
            if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]:
                current_nation_people = world_map[current_i][current_j]
                next_nation_people = world_map[next_i][next_j]
                people_gap = abs(current_nation_people - next_nation_people)

                if l <= people_gap <= r:
                    queue.append((next_i, next_j))
                    union.append((next_i, next_j))
                    visited[next_i][next_j] = 1
                    union_sum += next_nation_people
                    union_count += 1
                    is_moving = True

    for i, j in union:
        world_map[i][j] = union_sum // union_count

    return visited, is_moving


def moving(n, l, r):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    people_moving = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited, is_moving = bfs_union(n, i, j, l, r, visited)
                if is_moving:
                    people_moving = True
    return world_map, people_moving


N, L, R = map(int, input().split())
world_map = [list(map(int, input().split())) for _ in range(N)]
people_moving = True
answer = 0

while people_moving:
    people_moving = False
    world_map, people_moving = moving(N, L, R)
    if people_moving:
        answer += 1

print(answer)