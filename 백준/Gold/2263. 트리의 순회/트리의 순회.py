import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().strip().split()))
postorder = list(map(int, sys.stdin.readline().strip().split()))

node_index = [0] * (n + 1)
for i in range(n):
    node_index[inorder[i]] = i


def preorder(in_sp, in_ep, post_sp, post_ep):

    if (in_sp > in_ep) or post_sp > post_ep:
        return

    root = postorder[post_ep]

    root_index = node_index[root]
    left_len = root_index - in_sp
    right_len = in_ep - root_index

    ans.append(root)

    preorder(in_sp, root_index - 1, post_sp, post_sp + left_len -1)
    preorder(root_index + 1, in_ep, post_ep - right_len, post_ep-1)


ans = []
preorder(0, n-1, 0, n-1)
print(' '.join(map(str, ans)))