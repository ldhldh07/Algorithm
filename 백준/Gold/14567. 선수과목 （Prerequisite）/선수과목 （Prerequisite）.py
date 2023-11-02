import sys
from collections import deque

def topology_sort(n, adj_list, indegree):
    result = []
    queue = deque()
    answer = [1 for _ in range(n)]

    for i in range(n):
        if not indegree[i]:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)

        for next_node in adj_list[node]:
            indegree[next_node] -= 1
            if not indegree[next_node]:
                queue.append(next_node)
                answer[next_node] = answer[node] + 1

    return answer


si = sys.stdin.readline

N, M = map(int, si().strip().split())

adj_list = [[] for _ in range(N)]
indegree = [0 for _ in range(N)]

for _ in range(M):
    A, B = map(int, si().strip().split())

    adj_list[A-1].append(B-1)
    indegree[B-1] += 1

print(*topology_sort(N, adj_list, indegree), sep=" ")