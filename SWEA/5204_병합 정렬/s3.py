def merge(list_l, list_r, nl, nr):               # 리스트를 합치는 함수입니다
    list_result = [0] * (nl + nr)                # 최종 결과는 두 리스트의 갯수 합입니다
    i, j = nl - 1, nr - 1
    global cnt                                   # 큰수끼리 비교하는 값도 필요하기 때문에 큰수끼리 비교
    for a in range(nl + nr-1, -1, -1):           # 결과 리스트 왼쪽부터
        if i >= 0 and j >= 0:                    # 좌우 리스트 둘다 탐색이 다 안끝났을 때
            if list_l[i] <= list_r[j]:           # 우측 리스트의 현재 탐색중인 값이 더 크면
                list_result[a] = list_r[j]       # 리스트 오른쪽에 넣기
                j -= 1
            else:                                # 왼쪽이 더 크면 왼쪽에 넣기
                list_result[a] = list_l[i]
                i -= 1
                if a == nl+nr-1:                 # 맨처음 탐색했을 때 이 경우면
                    cnt += 1                     # 오른쪽 맨 끝값이 더 큰 경우에 포함
        elif i >= 0:                             # 왼쪽 있고 오른쪽 탐색 끝나면
            list_result[a] = list_l[i]           # 그냥 왼쪽 넣어주고
            i -= 1
        elif j >= 0:                             # 오른쪽 있고 왼쪽 탐색 끝났으면
            list_result[a] = list_r[j]           # 오른쪽 리스트 탐색중인 값 넣어주기
            j -= 1
    return list_result


def merge_sort(arr, n):                          # 분할하는 함수
    if n == 1:                                   # 갯수가 하나면
        return arr                               # 바로 그대로 반환
    else:
        s = n // 2                               # 중앙 값 정해주고
        left = merge_sort(arr[:s], n // 2)       # 좌, 우로 나누어주면서 재귀호출
        right = merge_sort(arr[s:], n // 2 + n % 2)
    return merge(left, right, n // 2, n // 2 + n % 2)  # 두개를 다시 합치면서 리턴


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, merge_sort(numbers, N)[N//2], cnt))  # 정렬된 함수 N // 2번째 값과 오른쪽이 더 커졌을 때 값