import sys
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def one_to_two(index):
    return divmod(index, 5)


def is_adjacent(start, combination):
    stack = [start]
    visited = [[False for _ in range(5)] for _ in range(5)]  # 5x5 배열 초기화
    count = 0
    
    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True  # 해당 위치 방문 표시
        count += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx >= 0 and nx < 5 and ny >= 0 and ny < 5) and ((nx, ny) in combination and not visited[nx][ny]):
                stack.append((nx, ny))
                
    return count == 7



def count_s(combination):
    return sum(1 for x, y in combination if students[x][y] == 'S')


si = sys.stdin.readline

students = [list(si().strip()) for _ in range(5)]

answer = 0
for comb in combinations(range(25), 7):
    two_d_comb = [one_to_two(index) for index in comb]
    
    if count_s(two_d_comb) >= 4:
        answer += (is_adjacent(two_d_comb[0], set(two_d_comb)))

print(answer)