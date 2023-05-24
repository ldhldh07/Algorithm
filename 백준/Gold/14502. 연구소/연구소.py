from itertools import combinations
import copy

def spread_virus(lab, n, m, vc):
    flag = True
    while flag:
        flag = False
        for x in range(n):
            for y in range(m):
                if lab[x][y] == 2:
                    for dx, dy in [[0, 1],[0,-1],[1,0],[-1,0]]:
                        next_x, next_y = x+dx, y+dy
                        if 0 <= next_x < n and 0 <= next_y < m:
                            if not lab[next_x][next_y]:
                                lab[next_x][next_y] = 2
                                vc -= 1
                                flag = True
    return vc


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

void_list = []
void_count = 0
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            void_list.append((i, j))
            void_count += 1
            
new_wall_list_list = combinations(void_list, 3)

max_void_count = 0
for new_wall_list in new_wall_list_list:
    new_lab = copy.deepcopy(lab)
    for new_wall_i, new_wall_j in new_wall_list:
        new_lab[new_wall_i][new_wall_j] = 1
    new_void_count = spread_virus(new_lab, N, M, void_count-3)
    max_void_count = max(max_void_count, new_void_count)

print(max_void_count)