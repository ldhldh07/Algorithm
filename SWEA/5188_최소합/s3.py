# 5188_최소합 풀이
# 2022-09-21

T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    min_arr = [[10 * (N-1) + 1] * (N+1) for _ in range(N+1)]     # 왼쪽이랑 위에 벽을 두고 더 작은 값으로 들어가지 않도록 값 설정 합니다.
    min_arr[1][1] = arr[0][0]                               # 첫자리만 최소합 배열에 넣어줍니다.

    for i in range(N):
        for j in range(N):
            if i != 0 or j != 0:                            # 첫자리 제외하고는 좌,상칸 중 더 최소합이 작은 값에서 현 위치의 값을 더해줍니다.
                min_arr[i+1][j+1] = (min_arr[i+1][j] if min_arr[i+1][j] < min_arr[i][j+1] else min_arr[i][j+1]) + arr[i][j]

    print('#{} {}'.format(t, min_arr.pop().pop()))