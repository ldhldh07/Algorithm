from collections import deque

def topology_sort(n, adj_list, indegree):
    result = []
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)
        for next_node in adj_list[node]:
            indegree[next_node] -= 1

            if not indegree[next_node]:
                queue.append(next_node)
