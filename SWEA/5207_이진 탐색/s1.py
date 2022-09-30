def binary_search(l, r, f, direction):           # 왼쪽, 오른쪽, 찾는 값, 이전방향
    global cnt                                   # 답을 찾았을 때 1씩 더해줄 함수
    m = (l + r) // 2                             # m 값 계산
    if list_a[m] == f:                           # 그 중앙값이 맞는 값이면
        cnt += 1                                 # 값 찾은 것이므로 cnt +1
    elif list_a[m] > f and direction != 1:       # 중앙값보다 찾는 값이 더 작으면 왼쪽으로
        binary_search(l, m-1, f, 1)              # 더 크면 오른쪽으로 보내서 재귀호출
    elif list_a[m] < f and direction != 0:       # 이전 방향과 같으면 호출 안함
        binary_search(m+1, r, f, 0)
    return


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    list_a = sorted(list(map(int, input().split())))
    list_b = list(map(int, input().split()))

    cnt = 0
    for b in list_b:                             # 리스트B에 있는 값들 하나씩 찾기
        binary_search(0, N-1, b, -1)
    print('#{} {}'.format(tc, cnt))