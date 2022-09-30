# 2105_디저트 카페 풀이
# 2022-09-25

def dessert(N):                                                 # 마름모를 덮는 큰 정사각형 모양을 생각
    for n in range(N-1, 0, -1):                                 # n : x+y고 답 나오면 바로 끝내도록 큰수부터 체크
        for x in range(1, n):                                   # x 값 결정
            y = n-x                                             # y 값
            for si in range(N-n):                               # 시작점 i는 밑에서 n까지 가능하며
                for sj in range(x, N-y):                        # j는 왼쪽에서는 x, 오른쪽에서 y까지 가능
                    i, j = si, sj
                    dessert_list = []                            # 해당 디저트 리스트
                    d = 0
                    for a in range(2 * n):
                        if arr[i][j] in dessert_list:            # 돌면서 같은 수 있으면 다음 경우로 넘어감
                            break
                        else:
                            dessert_list.append(arr[i][j])       # 있으면 리스트에 넣어줌
                            if i == si+n or j in [sj-x, sj+y]:  # 방향 바꾸는 지점은 사각형 만날때
                                d += 1
                            i, j = i + di[d], j + dj[d]
                    else:                                       # 같은수 만나서 종료되는 일 없으면
                        return 2 * n                            # 2 * n 반환
    return -1                                                   # 답 안나오면 -1 반환


T = int(input())

di = [1, 1, -1, -1]                                             # 우하, 좌하, 좌상, 우상
dj = [1, -1, -1, 1]

for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(t, dessert(N)))
