import heapq

def dijkstra(N, start_point, end_point, adj_list):
    cost_list = [10**8 for _ in range(N+1)]
    prev_node = [-1 for _ in range(N+1)]
    cost_list[start_point] = 0
    priority_queue = [(0, start_point)]

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if cost > cost_list[node]:
            continue
        
        for next_cost, next_node in adj_list[node]:
            new_cost = cost + next_cost
            if new_cost < cost_list[next_node]:
                cost_list[next_node] = new_cost
                prev_node[next_node] = node
                heapq.heappush(priority_queue, (new_cost, next_node))

    path = [end_point]
    while path[-1] != start_point:
        path.append(prev_node[path[-1]])
    path = path[::-1] 

    return cost_list[end_point], path




n = int(input())
m = int(input())

move_list = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, bus_cost = map(int, input().split())
    move_list[start].append((bus_cost, end))

bus_start_point, bus_end_point = map(int, input().split())
bus_cost, path = dijkstra(n, bus_start_point, bus_end_point, move_list)
print(bus_cost)
print(len(path))
print(*path)