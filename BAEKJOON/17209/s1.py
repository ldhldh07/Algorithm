from collections import deque

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
is_visited = [-1 for _ in range(N+1)]
ans = 0
for checked_student in range(1, N+1):
    group_count = [0, 0]
    if is_visited[checked_student] == -1:
        is_visited[checked_student] = 0
        group_count[0] += 1
        queue = deque([checked_student])
        while queue:
            current_student = queue.popleft()
            for next_student, reported_student_reported in enumerate(arr[current_student-1]):
                if reported_student_reported == 1 and is_visited[next_student+1] == -1:
                    is_visited[next_student+1] = 1 - is_visited[current_student]
                    group_count[is_visited[next_student+1]] += 1
                    queue.append(next_student + 1)

        ans += max(group_count)
print(ans)