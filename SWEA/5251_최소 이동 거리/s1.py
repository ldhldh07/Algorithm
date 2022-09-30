def dij(n):
    for i in range(1+n):
        cost_arr[i] = adjL[0][i]           # 정점별 비용 배열의 초기상태
    U = [0]                                # 이미 확인된 정점 배열으로 시작점 넣음
    for _ in range(n-1):                   # 출발점은 제외한 정점들의 수만큼 탐색하면 됨
        min_i = 0                          # 가장 비용이 적게 드는 정점 변수
        for i in range(1, n+1):            # 모든 정점 확인하면서
            if i not in U and cost_arr[i] < cost_arr[min_i]:  # 아직 확정이 안되어 있는 정점들 대상으로
                min_i = i                  # 가장 비용이 적은 정점 확인
        U.append(min_i)                    # 그 정점을 U에 넣고
        # 1부터 v 순회해서
        # min_i가 v랑 인접한 경우 v로 바로 가는 경우와 min_i거쳐 가는 것중 더 짧은 것
        for v in range(1, n+1):            # 출발선 제외한 정점 탐색
            if 0 < adjL[min_i][v] < 10 * (n-1):    # min_i 정점과 v 정점이 인접했을 때
                cost_arr[v] = min(cost_arr[min_i] + adjL[min_i][v], cost_arr[v])   # v를 거쳐서 가는 비용과 비교해서 작은값으로 갱신


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    cost_arr = [0] * (N+1)
    adjL = [[10 * (N-1)] * (N+1) for _ in range(N+1)]    # 초기값은 최대값으로
    for _ in range(E):
        b, c, d = map(int, input().split())
        adjL[b][c] = d                                   # 인접 배열에 가중치 입력

    dij(N)
    print('#{} {}'.format(tc, cost_arr.pop()))           # 마지막 정점까지 가는 비용 출력