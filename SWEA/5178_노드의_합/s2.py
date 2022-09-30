# 5178_노드의_합 풀이
# 2022-09-15

def calc(n):                                   # 좌측 노드와 우측 노드를 더하는 함수
    if not sum_list[n]:                        # 노드에 들어간 값이 0일때
        if 2 * n == N:                         # 마지막 값의 절반인 노드가 있을 때만
            return calc(2 * n)                 # 좌측 자식 노드 재귀호출해서 리턴
        return calc(2 * n) + calc(2 * n + 1)   # 나머지는 양쪽 더해서 재귀호출 리턴
    return sum_list[n]                         # 값이 있으면 그 값 리턴합니다.


T = int(input())

for t in range(1, 1+T):
    N, M, L = map(int, input().split())
    sum_list = [0] * (N + 1)
    for _ in range(M):                         # 입력값에서
        node, num = map(int, input().split())  # 숫자 쌍에서
        sum_list[node] = num                   # 왼쪽 숫자 인덱스 자리에 오른쪽 숫자 넣어줍니다

    print('#{} {}'.format(t, calc(L)))