from collections import deque

def bfs(N, M, arr):
    # 벽뚫기 남았을 때의 최단거리, 벽뚫기 안남았을때의 최단거리
    visited = [[[10**6, 10**6] for _ in range(M)] for _ in range(N)]
    # queue에 저장하는 값 : x, y, 벽뚫기 횟수, 최단거리
    queue = deque([(0,0,0,0)])
    while queue:
        
        x, y, cnt, dist =  queue.popleft()

        if x == M - 1 and y == N - 1:
            return dist + 1
        
        for move_x, move_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x, next_y = x + move_x, y + move_y

            if 0 <= next_x < M and 0 <= next_y < N:
                # 비어있고 거기로 갔을 때의 거리가 최단거리일 때
                if not arr[next_y][next_x] and dist + 1 < visited[next_y][next_x][cnt]:
                    visited[next_y][next_x][cnt] = dist + 1
                    # queue에 넣는데 cnt를 추가하지 않고 넣어버림
                    queue.append((next_x, next_y, cnt, dist + 1))
                # 벽일 경우 한칸 더감
                # 한칸 더 간게 빈칸이고 또 갈 수 있는 카운트가 남았을 때
                elif arr[next_y][next_x] and not cnt:
                    jump_x, jump_y = next_x + move_x, next_y + move_y
                    if 0 <= jump_x < M and 0 <= jump_y < N and not arr[jump_y][jump_x] and dist + 1 < visited[jump_y][jump_x][cnt+1]:
                        visited[jump_y][jump_x][cnt+1] = dist + 2
                        queue.append((jump_x, jump_y, cnt+1, dist + 2))

    return -1


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

print(bfs(N, M, arr))