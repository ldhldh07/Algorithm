from collections import deque

def topology_sort(n, adj_list):
    result = []
    queue = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for next_node in adj_list[node]:
            indegree[next_node] -= 1

            if not indegree[next_node]:
                queue.append(next_node)

    return result




N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    indegree[B] += 1

print(*topology_sort(N, adj_list))