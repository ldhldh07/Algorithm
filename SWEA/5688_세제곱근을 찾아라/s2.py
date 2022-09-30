T = int(input())
for t in range(1, 1 + T):
    N = int(input())
    for n in range(10 ** 6 + 1):           # 범위 내에서 가장 큰 세제곱근이 10**6이기 때문에 여기까지만 탐색합니다
        if n ** 3 == N:                    # N이 세제곱근일 경우
            print('#{} {}'.format(t, n))
            break                          # n출력하고 끝냅니다
        elif n ** 3 > N:                   # n의 3승이 N 넘어가는데도 값 안나왔으면
            print('#{} {}'.format(t, -1))  # -1 출력해줍니다
            break