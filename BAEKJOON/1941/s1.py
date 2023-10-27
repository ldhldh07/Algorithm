import sys

def dfs(x, y, visited, count_ds, count_dy, path):
    if count_ds + count_dy == 7:
        if count_ds >= 4:
            sorted_path = tuple(sorted(path))
            paths.add(sorted_path)
        return

    for d in range(4):
        nx, ny = x + di[d], y + dj[d]

        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            visited[nx][ny] = 1
            new_path = path + [(nx, ny)]
            if students[nx][ny] == 'S':
                dfs(nx, ny, visited, count_ds + 1, count_dy, new_path)
            else:
                dfs(nx, ny, visited, count_ds, count_dy + 1, new_path)
            visited[nx][ny] = 0

si = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

students = [list(si().strip()) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]

paths = set()

for i in range(5):
    for j in range(5):
        visited[i][j] = 1
        path = [(i, j)]
        if students[i][j] == 'S':
            dfs(i, j, visited, 1, 0, path)
        else:
            dfs(i, j, visited, 0, 1, path)
        visited[i][j] = 0

print(len(paths))
