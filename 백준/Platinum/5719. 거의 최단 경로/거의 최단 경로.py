import sys, heapq

def dijkstra(start, end, n, adjs):
    priority_queue = [(0, start)]
    distances = [float('inf') for _ in range(n)]
    prevs = [[] for _ in range(n)]
    distances[start] = 0

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distances[node]:
            continue

        for next_distance, next_node in adjs[node]:
            new_distance = distance + next_distance
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))
                prevs[next_node] = [node]
            elif new_distance == distances[next_node]:
                prevs[next_node].append(node)

    stack = [end]
    visited = set()

    while stack:
        current = stack.pop()
        for prev in prevs[current]:
            adjs[prev] = [(weight, node) for weight, node in adjs[prev] if node != current]
            if prev not in visited:
                stack.append(prev)
                visited.add(prev)
            
    priority_queue = [(0, start)]
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distances[node]:
            continue

        for next_distance, next_node in adjs[node]:
            new_distance = distance + next_distance
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))
                
    return distances[end] if distances[end] != float('inf') else -1

si = sys.stdin.readline

ans_list = []

while True:
    N, M = map(int, si().strip().split())
    if not N:
        break

    S, D = map(int, si().strip().split())

    adj_list = [[] for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, si().strip().split())
        adj_list[U].append((P, V))

    ans_list.append(dijkstra(S, D, N, adj_list))

print(*ans_list, sep='\n')