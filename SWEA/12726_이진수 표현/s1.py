# 10726_이진수 표현 풀이
# 2022-09-20

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    ans = 'ON'                       # 기본 답은 ON
    for n in range(N):               # 0~(N-1)까지 n으로 총 N개 확인
        if not M & (1 << n):         # n만큼 비트 이동해서 n번째 비트 값이 0이 나오면
            ans = 'OFF'              # 답 OFF로 변환
            break                    # 0 나온적 없으면 기본값인 ON 그대로
    print('#{} {}'.format(t, ans))