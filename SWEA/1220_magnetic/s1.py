# 1220_Magnetic 풀이
# 2022-08-19

T = 10

for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]        # 2차원 배열을 입력합니다.

    ans_count = 0                                                    # 위-> 아래로 볼 때 N 다음에 S가 나오면 교착상태입니다.

    for j in range(N):                                               # 행렬 뒤집은 방향으로 반복문을 합니다.
        last_mag = 0                                                 # 이전에 마지막으로 나왔던 자석 정보를 변수로 넣습니다.
        for i in range(N):
            if last_mag == 1 and arr[i][j] == 2:                     # 이전에 나왔던 자석이 N인 상황에서 S 나오면
                ans_count += 1                                       # 답 += 1
                last_mag = 2                                         # last_mag 최신화
            elif last_mag != 1 and arr[i][j] == 1:                   # 반대경우도 last_mag 최신화
                last_mag = 1
                                                                     # 이외의 경우는 결과값에 영향 없습니다.
    print('#{} {}'.format(t, ans_count))