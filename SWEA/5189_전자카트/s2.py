def cart(i, n, s):
    global min_battery                       # 최솟값 변수입니다
    if 0 not in visited:                     # 다 방문했을 때
        s += arr[i-1][0]                     # 최종방문지에서 사무실까지의 배터리량을 더해주고
        if s < min_battery:                  # 그 값이 최소값인지 확인합니다
            min_battery = s                  # 작을 경우 갱신합니다
    elif s >= min_battery:                   # 최종지 가기 전에도 이미 최솟값 넘어버리면
        return                               # 다른 경우 찾아봅니다
    else:
        for j in range(1, n+1):              # 2번부터 반복문 돌리면서
            if visited[j-1] == 0:            # 관리구역 방문 안했으면
                visited[j-1] = 1             # visited 표시하고
                cart(j, n, s + arr[i-1][j-1])  # 그 구역 시작으로 재귀호출합니다
                visited[j-1] = 0             # 재귀호출 끝난 후에는 다시 visited 없에줍니다


T = int(input())

for t in range(1, 1+T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)
    min_battery = 100 * N + 1                 # 모든 방문이 100이 들때가 최대값입니다

    visited[0] = 1
    cart(1, N, 0)
    print('#{} {}'.format(t, min_battery))
