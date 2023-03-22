from collections import deque

def bfs(K, W, H, arr):
    moves = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
    
    visited = [[[40000] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 0
    queue = deque([(0, 0, 0, 0)])
    
    while queue:
        x, y, horse_cnt, dist = queue.popleft()
        # print(queue)
        # print(visited)
        # print(horse_cnt)
        if x == H - 1 and y == W - 1:
            return dist

        for i, move in enumerate(moves):
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < H and 0 <= ny < W and not arr[nx][ny]:

                if i < 4:
                    new_horse_cnt = horse_cnt 
                elif horse_cnt < K: 
                    new_horse_cnt = horse_cnt + 1
                else:
                    continue 
                    
                if dist + 1 < visited[nx][ny][new_horse_cnt]:
                    visited[nx][ny][new_horse_cnt] = dist + 1
                    queue.append((nx, ny, new_horse_cnt, dist + 1))

    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

print(bfs(K, W, H, arr))