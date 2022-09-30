T = int(input())

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    bacteria = []
    for _ in range(K):
        a, b, n, d = map(int, input().split())
        bacteria.append([a, b, n, d])

    for _ in range(M):
        for i in range(K):
            bacteria[i][0] += di[bacteria[i][3]]
            bacteria[i][1] += dj[bacteria[i][3]]
            if not bacteria[i][0] or not bacteria[i][1]:
                bacteria[i][3] = bacteria[i][3] - 1 + 2 * (bacteria[i][3] % 2)
                bacteria[i][2] //= 2

        for a in range(K-1):
            same_place = [a]
            max_bac = bacteria[a][2]
            max_i = a
            sum_same = 0
            for b in range(a+1, K):
                if bacteria[a][0] == bacteria[b][0] and bacteria[a][1] == bacteria[a][1]:
                    same_place.append(b)
                    sum_same += bacteria[b][2]
                    if bacteria[b][2] > max_bac:
                        max_bac = bacteria[b][2]
                        max_i = b
            if len(same_place) > 1:
                for sp in same_place:
                    if sp == b:
                        bacteria[sp][2] = sum_same
                    else:
                        bacteria[sp][2] = 0

    print(bacteria)
    print(sum(bacteria[2]))
