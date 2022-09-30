T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]                    # 10x10 2차원 배열 생성
    purple_count = 0                                       # 보라색 갯수 초기값
    for _ in range(N):                                     # N번 칠하기
        r1 , c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):                          # i값은 r1 ~ r2
            for j in range(c1, c2+1):                      # j값은 c1 ~ c2
                if arr[i][j] == 0:                         # 색칠 안된 상태였으면
                    arr[i][j] = color                      # 현 color값 되게 해줌
                elif arr[i][j] + color == 3:               # 더해서 3이 뢷때
                    purple_count += 1                      # 보라색 갯수 +1

    print('#{} {}'.format(t, purple_count))

