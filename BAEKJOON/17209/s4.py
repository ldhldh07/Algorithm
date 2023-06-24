from collections import deque

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
is_visited = [-1 for _ in range(N+1)]
adj = [[] for _ in range(N+1)]
ans = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            adj[i+1].append(j+1)
            adj[j+1].append(i+1)

for checked_student in range(1, N+1):
    group_count = [0, 0]
    if is_visited[checked_student] == -1:
        is_visited[checked_student] = 0
        group_count[0] += 1
        queue = deque([checked_student])
        while queue:
            current_student = queue.popleft()
            for next_student in adj[current_student]:
                if is_visited[next_student] == -1:
                    is_visited[next_student] = 1 - is_visited[current_student]
                    group_count[is_visited[next_student]] += 1
                    queue.append(next_student)

        ans += max(group_count)
print(ans)
