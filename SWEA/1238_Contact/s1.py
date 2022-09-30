def bfs(v):                                  # bfs 탐색하면서 거리를 visited 배열에 입력하는 함수를 만듭니다
    queue = [0] * 101                        # 전화 가능한 점들의 정보를 담은 queue를 만들어줍니다
    front = rear = -1
    rear += 1                                # 시작점을 queue에 넣습니다
    queue[rear] = v
    visited[v] = 0                           # 시작점과의 거리와 전화했다는 사실을 기록해줍니다
    while front != rear:                     # 큐가 비어있을 때까지 반복
        front += 1                           # 전화 걸었으면 정점을 dequeue 해줍니다
        p = queue[front]
        for w in adjlist[p]:                 # 그 점에서 전화할 수 있는 점들을 반복합니다
            if visited[w] == -1:             # 전화하지 않았을 경우
                rear += 1                    # 그 점을 enqueue 해줍니다
                queue[rear] = w
                visited[w] = visited[p] + 1  # 이전 정점에서 +1 해준걸 기록해서 거리를 표현합니다


T = 10

for t in range(1, 1 + T):
    l, sp = map(int, input().split())
    arr = list(map(int, input().split()))
    adjlist = [[] for _ in range(101)]
    visited = [-1] * 101
    for i in range(l // 2):                  # 쌍으로 입력받은 값을 일방으로 간선 배열에 넣어줍니다
        start, end = arr[2 * i], arr[2 * i + 1]
        adjlist[start].append(end)

    bfs(sp)
    max_length = visited[1]
    max_v = 0
    for i, b in enumerate(visited):          # 거리가 최대값일 경우 중 정점 번호도 가장 큰 값을 구합니다
        if b >= max_length and i > max_v:
            max_length = b
            max_v = i
    print('#{} {}'.format(t, max_v))