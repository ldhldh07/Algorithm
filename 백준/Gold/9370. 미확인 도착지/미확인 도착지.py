import heapq


def dijkstra(start, n, adj):
    distance_list = [5 * 10 ** 7 for _ in range(n+1)]
    distance_list[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distance_list[node]:
            continue

        for next_distance, next_node in adj[node]:
            new_distance = distance + next_distance
            if new_distance < distance_list[next_node]:
                distance_list[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))

    return distance_list


T = int(input())

ans_list_list = []

for _ in range(T):


    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adj_list = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        adj_list[a].append((d, b))
        adj_list[b].append((d, a))

    candidate_points = list(int(input()) for _ in range(t))

    ans_list = []

    dist_from_s = dijkstra(s, n, adj_list)
    dist_from_g = dijkstra(g, n, adj_list)
    dist_from_h = dijkstra(h, n, adj_list)

    for candidate_point in candidate_points:
        dist_s_g_h_e = dist_from_s[g] + dist_from_g[h] + dist_from_h[candidate_point]
        dist_s_h_g_e = dist_from_s[h] + dist_from_h[g] + dist_from_g[candidate_point]
        dist_s_e = dist_from_s[candidate_point]
        if dist_s_g_h_e == dist_from_s[candidate_point] or dist_s_h_g_e == dist_from_s[candidate_point]:
            ans_list.append(candidate_point)

    ans_list.sort()
    ans_list_list.append(ans_list)

for ans_list in ans_list_list:
    print(*ans_list)