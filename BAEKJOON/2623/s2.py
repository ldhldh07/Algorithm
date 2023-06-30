from collections import deque

def topology_sort(V, adj_list):
    result = []
    queue = deque()

    for i in range(1, V+1):
        if not indegree[i]:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        result.append(node)

        for incoming_node in adj_list[node]:
            indegree[incoming_node] -= 1
            if not indegree[incoming_node]:
                queue.append(incoming_node)
    
    return result


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    length, *arr = map(int, input().split())
    prev_node = 0
    for node in arr:
        if prev_node:
            adj_list[prev_node].append(node)
            indegree[node] += 1
        prev_node = node

answer = topology_sort(N, adj_list)
            

print(*answer, sep='\n') if len(answer) == N else print(0)
