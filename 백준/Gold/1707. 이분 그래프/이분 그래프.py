from collections import deque

K = int(input())

ans_list = []

for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    visited = [0 for _ in range(V+1)]
    answer = True
    for num in range(1, V+1):
        if not visited[num]:
            queue = deque([num])
            visited[num] = 1
            while queue:
                current_num = queue.popleft()
                for next_num in adj_list[current_num]:
                    if not visited[next_num]:
                        visited[next_num] = 3 - visited[current_num]
                        queue.append(next_num)
                    elif visited[next_num] == visited[current_num]:
                        answer = False
                        break
                if not answer:
                    break
        if not answer:
            break
    ans_list.append("YES" if answer else "NO")

print(*ans_list, sep='\n')