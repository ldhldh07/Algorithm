T = int(input())


def node_cnt(n):
    if n:                                               # n이 0이 아닐때
        return node_cnt(ch1[n]) + node_cnt(ch2[n]) + 1  # 왼쪽 노드와 오른쪽 노드의 재귀호출 값을 더해주고 1을 더해줍니다
    return 0                                            # 0일때는 0으로 반환해줍니다


for t in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    arr = list(map(int, input().split()))
    ch1 = [0] * (V+1)                                   # 부모함수를 인덱스로 하는 왼쪽 자식 노드
    ch2 = [0] * (V+1)                                   # 부모함수를 인덱스로 하는 오른쪽 자식 노드

    for i in range(E):
        p, c = arr[2 * i], arr[2 * i + 1]               # 두 개씩 부모, 자식 쌍으로 입력받습니다
        if ch1[p] == 0:                                 # 자식 노드는 왼쪽이 비어있으면 왼쪽 자식 노드에
            ch1[p] = c
        else:                                           # 있으면 오른쪽 자식 노드에 넣어줍니다
            ch2[p] = c

    print('#{} {}'.format(t, node_cnt(N)))