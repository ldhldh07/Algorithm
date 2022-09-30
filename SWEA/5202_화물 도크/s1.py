# 5202_화물도크 풀이
# 2022-09-22

T = int(input())

for t in range(1, 1+T):
    N = int(input())
    se_list = []

    for _ in range(N):
        s, e = map(int, input().split())
        se_list.append((s, e))                                      # 시작시간과 종료시간을 튜플로 리스트에 넣어줍니다

    for i in range(N - 1, 0, -1):                                   # 버블정렬을 이용해 종료 시간 기준으로 오름차순 정렬합니다
        for j in range(i):
            if se_list[j][1] > se_list[j + 1][1]:
                se_list[j], se_list[j + 1] = se_list[j + 1], se_list[j]

    last_end = 0                                                    # 가장 마지막으로 한 작업이 끝난시간 저장
    cnt = 0                                                         # 작업한 횟수

    for s, e in se_list:                                            # 작업들을 반복문을 하며
        if s >= last_end:                                           # 마지막으로 끝난시간보다 시작시간이 나중이면 작업 실행합니다
            cnt += 1                                                # 횟수 더해주고
            last_end = e                                            # 끝난시간 갱신해줍니다

    print('#{} {}'.format(t, cnt))