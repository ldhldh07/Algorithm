from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = [-1] * (10 ** 5 + 1)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        for index, next_node in enumerate([node*2, node-1, node+1]):
            if 0 <= next_node < 10 ** 5 + 1 and visited[next_node] == -1:
                if index == 0:
                    visited[next_node] = visited[node]
                    queue.appendleft(next_node)
                else:
                    visited[next_node] = visited[node] + 1
                    queue.append(next_node)
    return visited[end]

start, end = map(int, input().split())
print(bfs(start, end))