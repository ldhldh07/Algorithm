def bfs(G, v, w):                              # G: 그래프, v시작점, w 도착점

    front = -1                                 # 초기 설정을 해줍니다

    rear = 0                                   # 시작점을 queue에 넣어줍니다
    queue[rear] = v
    visited[v] = 0                             # 방문 표기를 해줍니다

    while front - rear != 0:                   # 큐가 빌 때까지
        front += 1                             # 맨 앞의 값을 dequeue해줍니다
        t = queue[front]
        if t == w:                             # 최종점에 도착하면
            return visited[t]                  # 그 값까지 거리를 출력해줍니다
        for i in G[t]:                         # 정점에 인접한 점들의 목록을 호출합니다
            if visited[i] == -1:               # 방문한 적이 없으면
                rear += 1                      # enqueue해줍니다
                queue[rear] = i
                visited[i] = visited[t] + 1    # 이전 좌표의 값에서 +1해주어 거리를 기록합니다
    else:                                      # 다 돌고도 도착하지 못하면
        return 0                               # 0 출력합니다

T = int(input())

for t in range(1, 1+T):
    V, E = map(int, input().split())
    adjlist = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    visited = [-1] * (V+1)
    queue = [0] * (V+1)

    SP, EP = map(int, input().split())
    print('#{} {}'.format(t,bfs(adjlist, SP, EP)))
