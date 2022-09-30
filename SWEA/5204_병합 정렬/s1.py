def merge(list_l, list_r, nl, nr):               # 리스트를 합치는 함수입니다
    list_result = [0] * (nl + nr)                # 최종 결과는 두 리스트의 갯수 합입니다
    i = j = 0                                    # 각 리스트별 탐색하는 위치
    global cnt                                   # 마지막 값 두개 비교해서 오른쪽이 더 작은 경우 세는 변수
    if nl and nr:                                # 두 개 비교했을 때
        if list_l[nl-1] > list_r[nr-1]:
            cnt += 1
    for a in range(nl + nr):
        if i < nl and j < nr:
            if list_l[i] < list_r[j]:
                list_result[a] = list_l[i]
                i += 1
            else:
                list_result[a] = list_r[j]
                j += 1
        elif i < nl:
            list_result[a] = list_l[i]
            i += 1
        elif j < nr:
            list_result[a] = list_r[j]
            j += 1
    return list_result


def merge_sort(arr, n):
    if n == 1:
        return arr
    else:
        s = n // 2
        left = merge_sort(arr[:s], n // 2)
        right = merge_sort(arr[s:], n // 2 + n % 2)
    return merge(left, right, n // 2, n // 2 + n % 2)


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, merge_sort(numbers, N)[N//2], cnt))