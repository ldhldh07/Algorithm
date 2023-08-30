import sys
from collections import deque

def topology_sort(adjs, indegree, times, n):
    queue = deque()
    prefix_time = [0 for _ in range(n)]

    for i in range(n):
        if not indegree[i]:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        last_node = node

        for next_node in adjs[node]:
            indegree[next_node] -= 1
            prefix_time[next_node] = max(prefix_time[next_node], prefix_time[node] + times[node]) 

            if not indegree[next_node]:
                queue.append(next_node)

    return prefix_time[last_node] + times[last_node]


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