import sys
from collections import deque

def topology_sort(indegree, n, adjs):
    queue = deque()
    for i in range(n):
        if not indegree[i]:
            queue.append(i)
    
    while queue:
        node = queue.appendleft()
        print(node)
        for next_node in adjs[node]:
            indegree[next_node] -= 1
            if not indegree[next_node]:
                queue.append(next_node)
