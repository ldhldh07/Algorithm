def binary_tree(n):
    a = n // 2
    for i in range(1, a):
        ch1[i], ch2[i] = 2 * i, 2 * i + 1
        par[2 * i] = par[2 * i+1] = i

    if n % 2 == 0:
        ch1[a] = n
        par[n] = a
    else:
        ch1[a], ch2[a] = n-1, n
        par[n-1] = par[n] = a


T = int(input())


for t in range(1, 1+T):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    par = [0] * (N + 1)

    binary_tree(N)
    print(ch1)
    print(ch2)
    print(par)




