from collections import deque

def topology_sort(n, adjs, w):
    dp = [0 for _ in range(n+1)]
    queue = deque()

    for i in range(1, 1+n):
        if not indegree[i]:
            queue.append(i)
            dp[i] = building_times[i]

    while queue:
        node = queue.popleft()

        for next_node in adjs[node]:
            indegree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[node] + building_times[next_node])

            if not indegree[next_node]:
                queue.append(next_node)

    return dp[w]

T = int(input())
ans_list = []

for _ in range(T):
    N, K = map(int, input().split())
    building_times = [0] + list(map(int, input().split()))
    adj_list = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        adj_list[X].append(Y)
        indegree[Y] += 1

    W = int(input())

    ans_list.append(topology_sort(N, adj_list, W))

print(*ans_list, sep='\n')
