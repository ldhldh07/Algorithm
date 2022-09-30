def binary_tree(n):
    a = n // 2

    for i in range(1, a + (n % 2)):
        ch1[i], ch2[i] = 2 * i, 2 * i + 1
        par[2 * i] = par[2 * i + 1] = i

    if n % 2 == 0:
        ch1[a] = n
        par[n] = a


def input_tree(n):
    global idx
    if n:
        input_tree(ch1[n])
        ans_tree[n] = idx
        idx += 1
        input_tree(ch2[n])


T = int(input())

for t in range(1, 1 + T):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    par = [0] * (N + 1)
    ans_tree = [0] * (N + 1)
    idx = 1
    binary_tree(N)

    root = 1
    input_tree(root)
    print('#{} {} {}'.format(t, ans_tree[root], ans_tree[N//2]))