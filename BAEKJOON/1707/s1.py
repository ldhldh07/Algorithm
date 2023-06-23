from collections import deque

def is_bipartite(v, adj_list):
    visited = [0 for _ in range(v+1)]
    for num in range(1, v+1):
        if not visited[num]:
            queue = deque([num])
            visited[num] = 1
            while queue:
                current_num = queue.popleft()
                for next_num in adj_list[current_num]:
                    if not visited[next_num]:
                        visited[next_num] = 3 - visited[current_num]
                        queue.append(next_num)
                    elif visited[next_num] == visited[current_num]:
                        return 'NO'
    return 'YES'

K = int(input())

ans_list = []

for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    ans_list.append(is_bipartite(V, adj_list))

print(*ans_list, sep='\n')