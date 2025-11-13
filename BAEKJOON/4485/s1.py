import heapq

def dijkstra(n, start, adj_list, init):
    distance_list = [float("INF")] * n
    distance_list[start] = init

    priority_queue = [(init, start)]

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distance_list[node]: continue

        for next_node, next_cost in adj_list[node]:
            new_distance = next_cost + distance
            if new_distance < distance_list[next_node]:
                distance_list[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))

    return distance_list

def index(r, c, N):
    return r * N + c

num = 1
while True:
    N = int(input())
    if N == 0: break 

    cave = [list(map(int, input().split())) for _ in range(N)]
    adj_list = [[] for _ in range(N ** 2)]
    for i in range(N):
        for j in range(N):
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                adj_list[index(i, j, N)].append((index(ni, nj, N), cave[ni][nj]))

    dist = dijkstra(N ** 2, 0, adj_list, cave[0][0])

    print("Problem {}: {}".format(num, dist[index(N-1, N-1, N)]))
    num += 1