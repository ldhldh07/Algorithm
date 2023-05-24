from collections import deque

def bfs(K, W, H, arr):
    moves = [
        (-1, 0), (1, 0), (0, -1), (0, 1), # 일반 이동
        (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2) # 말 이동
    ]
    
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = True
    queue = deque([(0, 0, 0, 0)]) # x, y, horse_cnt, dist
    
    while queue:
        x, y, horse_cnt, dist = queue.popleft()

        if x == H - 1 and y == W - 1:
            return dist

        for i, move in enumerate(moves):
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < H and 0 <= ny < W and not arr[nx][ny]:
                if i < 4 or horse_cnt < K: # 일반 이동 또는 가능한 horse_cnt와 함께 말 이동
                    new_horse_cnt = horse_cnt + (i >= 4) # 말 이동이면 horse_cnt 증가
                    
                    if not visited[nx][ny][new_horse_cnt]:
                        visited[nx][ny][new_horse_cnt] = True
                        queue.append((nx, ny, new_horse_cnt, dist + 1))

    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

print(bfs(K, W, H, arr))