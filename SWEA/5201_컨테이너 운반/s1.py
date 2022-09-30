# 5201_컨테이너 운반_풀이
# 2022-09-22

def rev_sort(arr, n):                        # 오름차순 정렬 함수
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    products = rev_sort(list(map(int, input().split())), N)
    trucks = rev_sort(list(map(int, input().split())), M)
                                              # 제품과 트럭을 오름차순 정렬
    sum_p = 0
    test_i = 0
    while products and test_i <= M-1:         # 두 개를 순환하며
        if products[0] <= trucks[test_i]:     # 트럭을 태워갈 수있으면 제품을 더합니다
            sum_p += products.pop(0)
            test_i += 1
        else:                                 # 탈 수 있는 트럭이 없으면 그냥 다음 제품 봅니다
            products.pop(0)

    print('#{} {}'.format(tc, sum_p))