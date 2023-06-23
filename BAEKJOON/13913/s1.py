from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = [-1 for _ in range(10 ** 5 + 1)]
    prev = [0 for _ in range(10 ** 5 + 1)]
    visited[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            route = [node]
            last_node = node
            while not last_node == start:
                last_node = prev[last_node]
                route.append(last_node)
            return visited[node], route
        for next_node in (node-1, node+1, node*2):
            if 0 <= next_node < 10 ** 5 + 1 and visited[next_node] == -1:
                queue.append(next_node)
                prev[next_node] = node
                visited[next_node] = visited[node] + 1

start, end = map(int, input().split())
move_count, route_list = bfs(start, end)

print(move_count)
print(*reversed(route_list))