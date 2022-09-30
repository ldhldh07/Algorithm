def distance(x1, y1, x2, y2):
    return (x1-x2 if x1 > x2 else x2-x1) + (y1-y2 if y1 > y2 else y2-y1)   # 거리를 구하는 함수 선언


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
            dist_dict = {}                                                 # 시작점과 집들과의 거리가 들어갈 딕셔너리입니다
            house_cnt = 0                                                  # 탐색 거리에 따른 집 수입니다
            for a, b in houses:                                            # 거리별로 집의 갯수를 dict에 넣습니다
                if distance(i, j, a, b) not in dist_dict:
                    dist_dict[distance(i, j, a, b)] = 1
                else:
                    dist_dict[distance(i, j, a, b)] += 1
            for k in range(1 - N % 2 + N):                                 # 범위로 정할 k를 지도가 다 차는 범위까지로 해줍니다
                if not k:                                                  # k가 0일때만
                    margin -= 1                                            # 비용이 1 증가하고
                else:                                                      # 그 이후부터는
                    margin -= 4 * k                                        # 비용이 4의 배수씩 증가합니다

                if k in dist_dict:                                         # 그 거리에 해당하는 집이 있으면
                    margin += M * dist_dict[k]                             # 마진으로 M 곱한만큼 더해주고
                    house_cnt += dist_dict[k]                              # 집수도 더해줍니다

                if margin >= 0 and house_cnt > most_house:                 # 마진이 0이상인 상황에서 집 최댓값 갱신
                    most_house = house_cnt

    print('#{} {}'.format(t, most_house))
