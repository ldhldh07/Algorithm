from collections import deque

def topology_sort(n, adj_list, indegree, durations):
    queue = deque()
    times = [0 for _ in range(n)]

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
            times[i] = durations[i]

    while queue:
        node = queue.popleft()

        for next_node in adj_list[node]:
            indegree[next_node] -= 1
            times[next_node] = max(times[next_node], times[node] + durations[next_node])

            if not indegree[next_node]:
                queue.append(next_node)
                
    return times


N = int(input())

adj_list = [[] for _ in range(N)]
indegree = [0 for _ in range(N)]
durations = [0 for _ in range(N)]
for i in range(N):
    time, *prev_list, extra = list(map(int, input().split()))
    for prev in prev_list:
        adj_list[prev-1].append(i)
        indegree[i] += 1
    durations[i] = time

print(*topology_sort(N, adj_list, indegree, durations), sep='\n')
