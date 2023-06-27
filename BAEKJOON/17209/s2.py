from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(cur, old):
    if is_visited[cur] != -1: 
        return
    is_visited[cur] = old
    group_count[old] += 1
    for next_student, student_reported in enumerate(arr[cur]):
        if student_reported == 1 and is_visited[next_student] == -1:
            dfs(next_student, 1 - old)

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
is_visited = [-1 for _ in range(N)]
ans = 0
for checked_student in range(N):
    group_count = [0, 0]
    if is_visited[checked_student] == -1:
        dfs(checked_student, 0)
        ans += max(group_count)
print(ans)
