def partition(l, r):                         # 분할 함수
    pivot = arr[l]                           # 가장 앞의 값 피봇 설정
    i, j = l, r                              # 탐색 시작
    while i <= j:                            # 역전되기 전까지
        while i <= j and arr[i] <= pivot:    # 피봇보다 큰 값 나올 때까지 i 오른쪽으로
            i += 1
        while i <= j and arr[j] >= pivot:    # 피봇보다 작은 값 나올 때까지 j 오른쪽으로
            j -= 1
        if i < j:                            # j가 i보다 클 때 교환
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def qsort(l, r):                             # 퀵소트 재귀
    if l < r:
        s = partition(l, r)                  # 분할하면서 중앙값 반환
        qsort(l, s-1)                        # 왼쪽 재귀호출
        qsort(s+1, r)                        # 오른쪽 재귀호출


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    qsort(0, N-1)
    print('#{} {}'.format(tc, arr[N//2]))