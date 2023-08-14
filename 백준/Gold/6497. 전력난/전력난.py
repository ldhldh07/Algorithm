import sys, heapq


def prim(start, n, adj_list):
    priority_queue = [(0, start)]
    visited = [0 for _ in range(n)]
    result = 0

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if not visited[node]:
            visited[node] = 1
            result += cost

            for next_cost, next_node in adj_list[node]:
                if not visited[next_node]:
                    heapq.heappush(priority_queue, (next_cost, next_node))
    return result


si = sys.stdin.readline

ans_list = []

while True:

    m, n = map(int, si().strip().split())

    if (m, n) == (0, 0):
        break

    adj_list = [[] for _ in range(m)]
    max_cost = 0

    for _ in range(n):
        x, y, z = map(int, si().strip().split())
        adj_list[x].append((z, y))
        adj_list[y].append((z, x))
        max_cost += z

    ans_list.append(max_cost - prim(0, n, adj_list))

print(*ans_list, sep=" ")