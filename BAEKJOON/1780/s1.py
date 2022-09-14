import sys
sys.setrecursionlimit(10 ** 6)


def nine(sq_arr, l):
    nl = l // 3
    for n in range(9):
        square = []
        for i in range(nl * (n // 3), nl * (n // 3) + nl):
            for j in range(nl * (n % 3), nl * (n % 3) + nl):
                square.append(sq_arr[i][j])
        if len(list(set(square))) == 1:
            ans_dict[square.pop()] +=1
        else:
            n_square = []
            for a in range(nl):
                n_square.append([])
                for b in range(nl):
                    n_square[a].append(square[3*a+b])

            nine(n_square, nl)


N = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
ans_dict = {-1: 0, 0: 0, 1:0}
nine(arr, N)
print(ans_dict[-1])
print(ans_dict[0])
print(ans_dict[1])
