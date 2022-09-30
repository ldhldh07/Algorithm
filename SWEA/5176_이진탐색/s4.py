
def input_tree(n):                        # 2진트리에 전위순회하면서 인덱스 넣어주는 함수
    global idx
    if 2 * n <= N:
        input_tree(2 * n)
    ans_tree[n] = idx
    idx += 1
    if 2 * n + 1 <= N:
        input_tree(2 * n + 1)


T = int(input())

for t in range(1, 1 + T):
    N = int(input())

    ans_tree = [0] * (N + 1)
    idx = 1
    root = 1
    input_tree(root)                     # 값을 넣어줍니다
    print('#{} {} {}'.format(t, ans_tree[root], ans_tree[N//2]))  # 각 위치 출력합니다
