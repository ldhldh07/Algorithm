from collections import deque

# 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(start_i, start_j, n, m, arr, visited):
    queue = deque([(start_i, start_j)])
    while queue:
        current_i, current_j = queue.popleft()
        # 지금 체크하는 칸이 방문한 적이 없는 경우
        if 0 <= current_i < n and 0 <= current_j < m and not visited[current_i][current_j]:
            # 근데 그게 치즈 칸인 경우
            if arr[current_i][current_j]:
                # 들어오는 방향에 표시해줌 (왼쪽면이면 오른쪽으로 들어온걸로)
                arr[current_i][current_j]+= 1
            # 치즈칸이 아닌 경우
            else:
                # 방문 표시해주고
                visited[current_i][current_j] = 1
                # 큐에 넣어서 체크해준다
                for delta_i in range(4):
                    next_i, next_j = current_i + di[delta_i], current_j + dj[delta_i]
                    queue.append((next_i, next_j))
    return arr


N, M = map(int, input().split())
cheese_arr = [list(map(int, input().split())) for _ in range(N)]
cheese_visited = [[0 for _ in range(M)] for _ in range(N)]

ans = 0

while True:
    cheese_visited = [[0 for _ in range(M)] for _ in range(N)]
    cheese_arr = bfs(0, 0, N, M, cheese_arr, cheese_visited)
    ans += 1
    for i in range(N):
        for j in range(M):
            if 0 < cheese_arr[i][j] < 3:
                cheese_arr[i][j] = 1
            else:
                cheese_arr[i][j] = 0
    if not any(any(row) for row in cheese_arr):
        break
            

print(ans)