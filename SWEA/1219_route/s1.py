def dfs(v, visited):
    top = -1
    visited[v] = 1
    while True:
        for w in adjList[v]:                    # v점의 경로 w들 반복문
            if visited[w] == 0:                 # w 간적이 없으면
                top += 1                        # v 스택 쌓고
                stack[top] = v
                v = w                           # w로 이동
                visited[v] = 1
                break
        else:                                   # w 다해봤을 때, 즉 갈길 없을때
            if w != 99:                         # 최종점에 다다른 것이 아닌상황에
                if top != -1:                   # 시작점이 아니면
                    v = stack[top]              # 스택 pop해서 뒤로 갑니다
                    visited[v] = 0
                    top -= 1
                else:                           # 시작점에서 갈길 없는 상황이면 불가능하다는 것이므로
                    return 0                    # 0을 리턴합니다.
            else:                               # 최종점에 다다른 상태면
                return 1                        # 1을 리턴

T = 10
for t in range(1, 1+T):
    t,E = map(int, input().split())
    adjList = [[] for _ in range(100)]
    A = list(map(int, input().split()))
    visited = [0] * 100
    stack = [0] * 100

    for i in range(E):
        adjList[A[2 * i]].append(A[2 * i + 1])   # 홀수는 시작 짝수는 도착점으로 간선 입력

    print('#{} {}'.format(t, dfs(0, visited)))