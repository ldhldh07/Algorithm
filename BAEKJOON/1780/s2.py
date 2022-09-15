import sys
sys.setrecursionlimit(10 ** 6)


def nine(si, sj, l):
    last_num = arr[si][sj]
    for i in range(si, si + l):
        for j in range(sj, sj + l):
            if last_num != arr[i][j]:
                for a in range(3):
                    for b in range(3):
                        nl = l // 3
                        ni = si + a * nl
                        nj = sj + b * nl
                        nine(ni, nj, nl)
                return
    ans_dict[last_num] += 1


N = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
ans_dict = {-1: 0, 0: 0, 1: 0}
nine(0, 0, N)
print(ans_dict[-1])
print(ans_dict[0])
print(ans_dict[1])
