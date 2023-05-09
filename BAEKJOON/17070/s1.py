from collections import deque

N = int(input())

home = [[1] + list(map(int, input().split())) + [1] for _ in range(N)]
home = [[1] * (N + 2)] + home + [[1] * (N + 2)]

# 대각선인 경우 index : 1, 3, 5, 7 - %2 = 1
# 그냥 이동인 경우 index : 2, 4, 6, 8 - %2 = 0
delta_x = [0, 1, 1, 1, 0, -1, -1, -1]
delta_y = [1, 1, 0, -1, -1, -1, 0, 1]

# 45도 돌린다는건 delta의 인덱스 +-1 % 8


# 첫 방향은 오른쪽
first_direction = 0

# 첫 끝 위치
first_end_x = 1
first_end_y = 2
queue = deque([(first_end_x, first_end_y, first_direction)])
cnt = 0
# BFS 돌림

while queue:
    current_end_x, current_end_y, current_direction = queue.popleft()

    if current_end_x == N and current_end_y == N:
        cnt += 1
        continue

    for next_direction in [
        (current_direction - 1) % 8,
        current_direction,
        (current_direction + 1) % 8,
    ]:
        # 우하일때
        if next_direction == 1:
            # 가는 곳과 그 방향 -+1 위치가 0인경우에만
            for check_direction in [
                (next_direction - 1) % 8,
                (next_direction + 1) % 8,
                next_direction,
            ]:
                check_end_x = current_end_x + delta_x[check_direction]
                check_end_y = current_end_y + delta_y[check_direction]
                if home[check_end_x][check_end_y]:
                    break
            else:
                # 그 방향으로 이동(deque에 넣어버림)
                next_end_x, next_end_y = check_end_x, check_end_y
                queue.append((next_end_x, next_end_y, next_direction))
        # 대각선 아닌 방향으로 갈때
        elif next_direction in [0, 2]:
            next_end_x, next_end_y = (
                current_end_x + delta_x[next_direction],
                current_end_y + delta_y[next_direction],
            )
            if not home[next_end_x][next_end_y]:
                queue.append((next_end_x, next_end_y, next_direction))
print(cnt)
