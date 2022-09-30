# 1861_정사각형 방 풀이
# 2022-09-16

def move_room(si, sj):                                  # 방을 옮기는 함수를 만듭니다
    global room_cnt                                     # 방 갯수 변수
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 델타탐색
        ni, nj = si + di, sj + dj                       # 다음방 좌표
        if arr[ni][nj] == arr[si][sj] + 1:              # 다음방 값이 지금값보다 1 크면
            room_cnt += 1                               # 방갯수 1 더해주고
            move_room(ni, nj)                           # 이동한 방을 원소로 재귀호출해줍니다
            break                                       # 1 큰값은 어차피 하나뿐이니 for문은 끝내줍니다
    return room_cnt                                     # 갈곳 없으면 cnt값 반환합니다


T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
    len_list = [0] * (N * N + 1)                        # 숫자를 인덱스로 이동하는 방 갯수를 넣어줍니다

    for i in range(1, 1+N):                             # 전체 방 반복
        for j in range(1, 1+N):
            room_cnt = 1                                # 방갯수는 탐색 전에 초기화해줍니다
            len_list[arr[i][j]] = move_room(i, j)       # 방문한 방 수를 함수로 구해 전체 리스트에 넣어줍니다

    max_cnt = 1
    for i, ll in enumerate(len_list):                   # 방수 리스트를 순회하면서
        if ll > max_cnt:                                # 최대값보다 클 때만 갱신되도록 하면
            max_cnt = ll                                # 가장 인덱스 낮은 값이 들어갑니다
            min_startroom = i

    print('#{} {} {}'.format(t, min_startroom, max_cnt))