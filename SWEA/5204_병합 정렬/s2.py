def merge(list_l, list_r):
    list_result = []
    while list_l or list_r:
        if list_l and list_r:
            if list_l[0] < list_r[0]:
                list_result.append(list_l.pop(0))
            else:
                list_result.append(list_r.pop(0))
        elif list_l:
            list_result.append(list_l.pop(0))
        elif list_r:
            list_result.append(list_r.pop(0))
    return list_result


def merge_sort(arr, n):
    if n == 1:
        return arr
    else:
        s = n // 2
        left = merge_sort(arr[:s], n // 2)
        right = merge_sort(arr[s:], n // 2)
    return merge(left, right)


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input().split()))

    print(merge_sort(numbers, N))