import sys
from collections import deque

def topology_sort(adjs, indegree, times, n):
    queue = deque()
    durations = [0 for _ in range(n)]

    for i in range(n):
        if not indegree[i]:
            queue.append(i)
            durations[i] = times[i]
    
    while queue:
        node = queue.popleft()

        for next_node in adjs[node]:
            indegree[next_node] -= 1
            durations[next_node] = max(durations[next_node], durations[node] + times[next_node]) 

            if not indegree[next_node]:
                queue.append(next_node)

    return max(durations)

si = sys.stdin.readline

N = int(si().strip())

times = [0 for _ in range(N)]
adj_list = [[] for _ in range(N)]
indegree = [0 for _ in range(N)]

for work_index in range(N):
    time, prev_length, *prevs = map(int, si().strip().split())
    times[work_index] = time
    for prev in prevs:
        adj_list[prev-1].append(work_index)
    indegree[work_index] = prev_length

print(topology_sort(adj_list, indegree, times, N))