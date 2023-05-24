from collections import deque


def dfs(sp):
    v = sp
    for w in adjList[v]:
        if w not in know_list:
            know_list.append(w)
            dfs(w)


N, M = map(int, input().split())
know_list = deque(map(int, input().split()))
len_know = know_list.popleft()
know_list = list(know_list)
pl = []
adjList = [[] for _ in range(N + 1)]

for _ in range(M):
    pms = deque(map(int, input().split()))
    len_pm = pms.popleft()
    pms = list(pms)
    for i in range(len_pm - 1):
        for j in range(i + 1, len_pm):
            adjList[pms[i]].append(pms[j])
            adjList[pms[j]].append(pms[i])
    pl.append(pms)

for n in know_list:
    dfs(n)

ans = 0

for party in pl:
    for party_member in party:
        if party_member in know_list:
            break
    else:
        ans += 1

print(ans)