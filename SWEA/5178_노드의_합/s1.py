def calc(n):                        # 좌측 노드와 우측 노드를 더하는 함수
    sum_node = sum_list[n]          # 현재 입력된 값을 가져옵니다
    if n * 2 <= N:                  # 좌측 노드가 존재하면
        sum_node += calc(2 * n)     # 좌측 노드를 더해줍니다
    if n * 2 + 1 <= N:              # 우측 노드가 존재하면
        sum_node += calc(2 * n + 1)
    return sum_node


T = int(input())

for t in range(1, 1+T):
    N, M, L = map(int, input().split())
    sum_list = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        sum_list[node] = num

    print(calc(L))
