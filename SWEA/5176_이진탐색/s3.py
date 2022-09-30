# 5176_이진탐색 풀이
# 2022-09-15

def binary_tree(n):                       # 이진트리 부모노드를 인덱스로 자식 노드 만드는 함수
    a = n // 2                            # n : 마지막 노드
    for i in range(1, a + (n % 2)):       # 자식 노드에 노드의 2배, 2배 + 1 넣어줍니다
        ch1[i], ch2[i] = 2 * i, 2 * i + 1
    if n % 2 == 0:                        # 한쪽만 있을 때는 왼쪽에만 넣어줍니다
        ch1[a] = n


def input_tree(n):                        # 2진트리에 전위순회하면서 인덱스 넣어주는 함수
    global idx                            # idx 사용
    if n:                                 # n이 0이 아닐때
        input_tree(ch1[n])                # 왼쪽 재귀호출
        ans_tree[n] = idx                 # 인덱스 값만큼 넣어줍니다
        idx += 1                          # 인덱스 1 더해줍니다
        input_tree(ch2[n])                # 오른쪽 재귀호출


T = int(input())

for t in range(1, 1 + T):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    ans_tree = [0] * (N + 1)
    idx = 1
    binary_tree(N)                       # 2진 트리 만들어줍니다
    root = 1
    input_tree(root)                     # 값을 넣어줍니다
    print('#{} {} {}'.format(t, ans_tree[root], ans_tree[N//2]))  # 각 위치 출력합니다