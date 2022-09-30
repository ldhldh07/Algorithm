T = 1

di = [0, 1, 0, -1]                                                    # 우, 하, 좌, 상 델타탐색
dj = [1, 0, -1, 0]

for _ in range(1, 1+T):
    t = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(3)]
    
    print(arr)                                                                  # 양쪽에 더미 한줄씩 넣어줌
    # k = 3                                                             # 첫 방향은 위
    # i = 99                                                            # 가장 아래에서 시작
    # j = 0                                                             # 일단 0으로 초기화

    # for a in range(1, 101):
    #     if arr[99][a] == 2 :
    #         j = a                                                     # 시작하는 j값 탐색

    # while i > 0 :                                                     # 도착하기 전까지 while문
    #     if arr[i + di[3 - (k % 2)]][j + dj[3 - (k % 2)]] == 1:        # 방향이 위일때는 좌우, 좌우일때는 위로 갔을 때 1인지 확인
    #         k = 3 - (k % 2)                                           # 있으면 그쪽으로 방향 전환
    #     elif arr[i + di[1 - (k % 2)]][j + dj[1 - (k % 2)]] == 1:      # 아래로 안가게 위부터 탐색하게 위 먼저
    #         k = 1 - (k % 2)

    #     i += di[k]                                                    # 바뀐 방향으로 하나씩 이동
    #     j += dj[k]

    # print('#{} {}'.format(t, j-1))


