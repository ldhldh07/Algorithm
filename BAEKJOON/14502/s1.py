from itertools import combinations
from collections import deque

def spread_virus(lab, virus, wall, n):
    while True:
        for virus_i, virus_j in virus:
            for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                next_virus_i, next_virus_j = virus_i + di, virus_j + dj
                if (next_virus_i, next_virus_j) not in wall and (next_virus_i, next_virus_j) not in virus:
                    virus.append((next_virus_i, next_virus_j))
                    lab[next_virus_i][next_virus_j] = 1
                

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

virus_list = deque()
wall_list = deque()
void_list = deque()

for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus_list.append((i, j))
        elif lab[i][j] == 1:
            wall_list.append((i, j))
        elif lab[i][j] == 0:
            void_list.append((i, j))
            
new_wall_list_list = combinations(void_list, 3)

for new_wall_list in new_wall_list_list:
    renewal_wall_list = wall_list.copy()
    renewal_wall_list.extend(new_wall_list)
    print(renewal_wall_list)
        
        