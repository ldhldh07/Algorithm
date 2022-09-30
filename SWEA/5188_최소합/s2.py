# 5188_최소합 풀이
# 2022-09-21

def move(x, y, n, s):                                # x, y: 좌표, n: 한면 길이, s 이동한 지점까지의 합
    global min_route                                 # 최소 합이 들어가는 글로벌 변수
    if x == (n-1) and y == (n-1):                    # 최종목적지(오른쪽 아래) 도착했을 때
        if s < min_route:                            # 합이 최소값보다 작으면 갱신
            min_route = s
    elif s >= min_route:                             # 이동 중에 이미 최솟값 넘으면 탐색 중단
        return
    else:                                            # 위 경우 아닐 때 탐색
        for dx, dy in [[0,1], [1,0]]:                # 오른쪽, 아래 이동
            nx, ny = x + dx, y + dy                  # 다음 좌표
            if arr[nx][ny]:                          # 벽이 아닐때
                move(nx, ny, n, s + arr[nx][ny])     # 합 담아서 이동


T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]

    min_route = 10 * (2 * N -1)
    move(0, 0, N, arr[0][0])                         # 0,0에서의 값 넣어서 함수
    print('#{} {}'.format(t, min_route))