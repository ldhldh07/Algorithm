from collections import deque


def bfs(start, end):
    queue = deque([start, 0])
    # visited = [-1 for _ in range(10 ** 5 + 1)]
    # #[걸린 시간, k의 위치]
    # visited[start] = 0

    while queue:
        node, time = queue.popleft()
        for next_node in [node*2, node-1, node+1]:
            if 0 <= next_node < 10 ** 5 + 1 and visited[next_node] == -1:
                visited[next_node] = visited[node]
                queue.appendleft(next_node)

    return visited[end]

start, end = map(int, input().split())

num = 0
num_list = [0]
while num <= 10* 5:
    num += 1
    num_list.append(num)


print(bfs(start, end))