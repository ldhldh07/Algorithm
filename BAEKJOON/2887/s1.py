import heapq

def binary_search(planet_list, list_length, target, criteria):
    planet_list.sort(key=lambda item:item[criteria])
    start = 0
    end = list_length-1
    min_cost = float('inf')
    min_node = None

    while start < end:
        mid = (start + end) // 2
        cost = abs(planet_list[mid][criteria] - target)
        
        if cost < min_cost:
            min_cost = cost
            min_node = planet_list[mid][3]

        if planet_list[mid][criteria] < target:
            start = mid+1
        else:
            end = mid -1

    return min_cost, min_node
    

def prim(start, n, planets):
    priority_queue = [(0, start)]
    visited = [0 for _ in range(n+1)]

    sum_cost = 0

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if visited[node]:
            continue

        sum_cost += cost
        print(cost, node)
        visited[node] = 1

        for criteria in range(3):
            target = planets[node][criteria]
            next_cost, next_node = binary_search(planets, n, target, criteria)
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_cost, next_node))

    return sum_cost

N = int(input())
planets = [tuple(map(int, input().split()))+(index,) for index in range(N)]
print(prim(0, N, planets))
