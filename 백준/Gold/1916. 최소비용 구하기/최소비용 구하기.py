import heapq

def dijkstra(n, sp, ep, adj_list):
    cost_list = [10**8 for _ in range(n+1)]
    cost_list[sp] = 0
    priority_queue = [(0,sp)]

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        
        if cost > cost_list[node]:
            continue

        for next_cost, next_node in adj_list[node]:
            new_cost = cost + next_cost
            if new_cost < cost_list[next_node]:
                cost_list[next_node] = new_cost
                heapq.heappush(priority_queue, (new_cost, next_node))
    return cost_list[ep]

N = int(input())
M = int(input())

move_list = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    move_list[s].append((cost, e))
    
start_point, end_point = map(int, input().split())
move_cost = dijkstra(N, start_point, end_point, move_list)

print(move_cost)