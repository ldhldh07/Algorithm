# from collections import deque
import sys
sys.setrecursionlimit(100000)

def bfs(x, y, horse_cnt):

    for move in [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]:
        
        nx, ny = x + move[0], y + move[1]
        # print(nx, ny)
        if 0 <= nx < H and 0 <= ny < W and not arr[nx][ny] and visited[nx][ny] > visited[x][y] + 1:
            visited[nx][ny] = visited[x][y] + 1
            if move in [[2,1],[2,-1],[-2,1],[-2,-1]]:
                if not horse_cnt:
                    return
                else:
                    bfs(nx, ny, horse_cnt - 1)
            else:
                bfs(nx, ny, horse_cnt)


K = int(input())

W, H = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[40000] * W for _ in range(H)]


# print(arr)
# print(visited)
start_x, start_y = 0, 0 
visited[start_x][start_y] = 0
# queue = deque((0, 0))
bfs(start_x, start_y, K)

# print(visited)
# print(H, W)
print(-1 if visited[H-1][W-1] == 40000  else visited[H-1][W-1])