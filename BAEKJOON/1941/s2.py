import sys

def dfs(i, j):
    global answer
    stack = [(i, j, [(i, j)], 1 if students[i][j] == 'S' else 0)] 
    
    while stack:
        x, y, path, s_count = stack.pop()
        
        if len(path) == 7:
            if s_count >= 4:
                answer += 1
            continue
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in path:
                next_s_count = s_count + (students[nx][ny] == 'S')
                stack.append((nx, ny, path + [(nx, ny)], next_s_count))

si = sys.stdin.readline

answer = 0 

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

students = [list(si().strip()) for _ in range(5)]


for i in range(5):
    for j in range(5):
        dfs(i, j)

print(answer) 