T = int(input())

for tc in range(1, 1+T):
    arr = list(map(int, input().split()))
    cnt = 0
    i = arr[0]                              # 맨 뒤 정거장을 시작점으로 함
    while i != 1:                           # 맨 처음 정거장 갈때까지
        for a in range(1, i):               # 가능한 가장 먼 정류장으로 이동
            if arr[a] >= i-a:               # 배터리가 남은 거리 이상일 때
                i = a                       # 정류장 이동하고
                cnt += 1                    # 카운트
                break

    print('#{} {}'.format(tc, cnt-1))