T = int(input())

for t in range(1, 1+T):
    N, M = map(int, input().split())  # N : 도시의 크기, M : 집 비용

    town = [list(map(int, input().split())) for _ in range(N)]

    houses = []                                                            # 매번 모든 공간을 탐색하기보다는 전체 비용은 공식으로 구하고
                                                                           # 거리 이내에 있는 집의 수만큼 지불액을 뺐습니다
    for x in range(N):                                                     # 집의 좌표를 리스트에 모아둡니다
        for y in range(N):
            if town[x][y]:
                houses.append((x, y))

    most_house = 0                                                         # 가장 많은 집수가 들어갈 변수입니다

    for i in range(N):
        for j in range(N):                                                 # 탐색 시작점을 정하고
            margin = 0                                                     # 시작점마다 마진을 초기화합니다
            for k in range(1 - N % 2 + N):                                 # 범위로 정할 k를 지도가 다 차는 범위까지로 해줍니다
                house_cnt = 0
                for a, b in houses:
                    if (i-a if i > a else a-i) + (j-b if j > b else b-j) <= k:
                        house_cnt += 1
                if house_cnt * M - (k ** 2 + (k-1) ** 2)>= 0 and house_cnt > most_house:                 # 마진이 0이상인 상황에서 집 최댓값 갱신
                    most_house = house_cnt

    print('#{} {}'.format(t, most_house))
