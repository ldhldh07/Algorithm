from collections import deque

def bfs(start_node, N):
    visited = [-1] * (N+1)
    visited[start_node] = 0
    max_node = start_node
    max_distance = 0

    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        for next_node, distance in adj_list[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + distance
                queue.append(next_node)
                if visited[next_node] > max_distance:
                    max_distance = visited[next_node]
                    max_node = next_node
    return (max_node, max_distance)


n = int(input())

adj_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, distance = map(int, input().split())
    adj_list[s].append((e, distance))
    adj_list[e].append((s, distance))

longest_length_start_node = bfs(1, n)[0]
print(bfs(longest_length_start_node, n)[1])