import heapq

def dijkstra(n, start, adjList):
    distance_list = [10**5] * (n + 1)
    distance_list[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        # print('빼기전', priority_queue)
        distance, node = heapq.heappop(priority_queue)
        # print('큐에서 뺀거', distance, node)
        # print('뺀 후', priority_queue)

        # print('distance_list[node]', distance_list[node])
        # print('distance', distance)
        if distance_list[node] < distance:
            continue

        for next_distance, next_node in adjList[node]:
            print('next_node, cost',next_node, next_distance)
            new_distance = distance + next_distance
            if new_distance < distance_list[next_node]:
                distance_list[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))
    return distance_list


N, M, X = map(int, input().split())

adjList = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, Ti = map(int, input().split())
    adjList[s].append((e, Ti))

X_distance_list = dijkstra(N, X, adjList)
max_ans = 0
for a in range(1, 1+N):
    ans = dijkstra(N, a, adjList)[X] + X_distance_list[a]
    if max_ans < ans:
        max_ans = ans

print(max_ans)