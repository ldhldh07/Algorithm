def ride(x1, y1, x2, y2):                          # 두 칸 사이 이동하는 함수
    if arr[x2][y2] > arr[x1][y1]:                  # 이동하는 곳이 더 높으면
        return arr[x2][y2] - arr[x1][y1] + 1       # 높이 차이 + 1만큼
    else:
        return 1                                   # 아닐때는 그냥 1


def move(x, y, n):                                 # 산 돌아다니는 함수 x, y : 시작 좌표, n은 변 길이
    queue = [(x, y)]                               # 큐에 시작 좌표 넣어주고
    while queue:                                   # 다 확인할때까지
        i, j = queue.pop(0)                        # 가장 처음에 넣은 걸 먼저 확인하고
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj                # 상하좌우로 이동했을 때
            if 0 <= ni < n and 0 <= nj < n:        # 이동 가능한 범위면
                if visited[ni][nj] > visited[i][j] + ride(i,j,ni,nj): # 이동할때 그 전에 기록된 해당 산까지의 비용보다 작을 때
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + ride(i,j,ni,nj)  # 그 점으로 이동
    return visited.pop().pop()                     # 마지막 값 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1001 * N * N] * N for _ in range(N)]
    visited[0][0] = 0

    min_route = 1001 * N * N
    queue = []

    print('#{} {}'.format(tc, move(0, 0, N)))
