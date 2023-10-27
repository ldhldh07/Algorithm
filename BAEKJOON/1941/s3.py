def dfs(x, y, visited, count_ds, count_dy):
    global answer
    
    if count_ds + count_dy == 7:
        if count_ds >= 4:
            answer += 1
        return

    for d in range(4):
        nx, ny = x + di[d], y + dj[d]
        
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            visited[nx][ny] = 1
            
            if students[nx][ny] == 'S':
                dfs(nx, ny, visited, count_ds + 1, count_dy)
            else:
                dfs(nx, ny, visited, count_ds, count_dy + 1)
            
            visited[nx][ny] = 0

# Uncomment this line when you run the code from a terminal
# si = sys.stdin.readline

# Uncomment these lines when you run the code from a terminal
# students = [list(si().strip()) for _ in range(5)]

# Hardcoding the input for demonstration
students = [
    ['S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S'],
]

visited = [[0 for _ in range(5)] for _ in range(5)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

answer = 0

for i in range(5):
    for j in range(5):
        visited[i][j] = 1
        if students[i][j] == 'S':
            dfs(i, j, visited, 1, 0)
        visited[i][j] = 0

print(answer)
