from collections import deque
import sys
sys.setrecursionlimit(10**5)

def bfs(start_node, v):
    visited = [-1] * (v+1)
    visited[start_node] = 0
    queue = deque([start_node])
    max_distance = 0
    max_node = start_node

    while queue:
        # 다음으로 이동하는 node
        node = queue.popleft()
        # 시작점에서 visited의 index값에 해당되는 노드들과의 거리
        for next_node, distance in adjList[node]:
            # 방문한 적이 없다면
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + distance
                queue.append(next_node)
                if visited[next_node] > max_distance:
                    max_distance = visited[next_node]
                    max_node = next_node
    return (max_node, max_distance)



V = int(input())

adjList = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1, 2):
        adjList[arr[0]].append([arr[i], arr[i+1]])

one_of_longest_node = bfs(1, V)[0]
final_max_distance = bfs(one_of_longest_node, V)[1]

print(final_max_distance)