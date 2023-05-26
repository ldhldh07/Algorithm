from collections import deque

def solution(n, edges):
    
    def bfs(sp):
        queue = deque([sp])
        visited[sp] = 1
        
        while queue:
            node = queue.popleft()
            for next_node in adj_list[node]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = visited[node] + 1
    
    adj_list = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    for edge in edges:
        s, e = edge
        adj_list[s].append(e)
        adj_list[e].append(s)
    
    bfs(1)
    a = max(visited)
    answer = visited.count(a)
        
        
    return answer