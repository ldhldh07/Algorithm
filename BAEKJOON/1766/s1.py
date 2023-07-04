from collections import deque
import heapq

def topology_sort(n, adjs):
    result = []
    priority_queue = []
    for i in range(1, 1+n):
        if not indegree[i]:
            heapq.heappush(priority_queue, i)

    while priority_queue:
        num = heapq.heappop(priority_queue)
        result.append(num)
        for next_num in adjs[num]:
            indegree[next_num] -= 1
            if not indegree[next_num]:
                heapq.heappush(priority_queue, next_num)

    return result

N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    indegree[B] += 1

print(*topology_sort(N, adj_list))
