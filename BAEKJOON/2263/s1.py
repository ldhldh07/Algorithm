import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().strip().split()))
postorder = list(map(int, sys.stdin.readline().strip().split()))

node_index = [0] * (n + 1)

for i in range(n):                    # inorder에서 각 값의 인덱스 저장
    node_index[inorder[i]] = i


def preorder(in_sp, in_ep, post_sp, post_ep):

    if (in_sp > in_ep) or post_sp > post_ep:  # 이 조건에 해당되면 자연스럽게 종료
        return

    root = postorder[post_ep]                 # 후위식의 맨 뒤가 루트 노드

    root_index = node_index[root]             # 루트 노드가 위치한 값
    left_len = root_index - in_sp             # 왼쪽 길이
    right_len = in_ep - root_index            # 오른쪽 길이

    ans.append(root)                          # 루트 노드 값 출력

    preorder(in_sp, root_index - 1, post_sp, post_sp + left_len -1)  # 왼쪽으로 재귀호출
    preorder(root_index + 1, in_ep, post_ep - right_len, post_ep-1)  # 오른쪽 재귀호출


ans = []
preorder(0, n-1, 0, n-1)
print(' '.join(map(str, ans)))