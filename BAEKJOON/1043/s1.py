from collections import deque


def dfs(sp):                               # 같은 파티에 포함된적이 있는 사람들을 다 포함시키는 함수를 만듭니다.
    v = sp
    for w in adjList[v]:
        if w not in know_list:
            know_list.append(w)
            dfs(w)                         # 포함되면 다시 그 사람을 가지고 탐색을 하게끔 재귀호출을 해줍니다


N, M = map(int, input().split())           # 전체 사람과 파티 수를 받습니다.
know_list = deque(map(int, input().split())) # 리스트 받은 것에서
len_know = know_list.popleft()             # 초기에 진실을 아는 사람들의 수를 리스트에서 뺴고
know_list = list(know_list)                # 리스트를 구합니다.
pl = []                                    # 파티의 리스트를 만듭니다
adjList = [[] for _ in range(N + 1)]       # 서로간 연결관계를 기록할 그래프를 만듭니다

for _ in range(M):
    pms = deque(map(int, input().split()))
    len_pm = pms.popleft()                 # 파티 멤버수와
    pms = list(pms)                        # 파티 리스트를 구합니다
    for i in range(len_pm - 1):            # 같은 파티에 있으면 그래프로 이어지게 합니다
        for j in range(i + 1, len_pm):
            adjList[pms[i]].append(pms[j])
            adjList[pms[j]].append(pms[i])
    pl.append(pms)                         # 파티는 파티 리스트에 넣습니다

for n in know_list:                        # 초기 리스트에서부터 시작해서 아는 사람들을 리스트에 담습니다
    dfs(n)

ans = 0

for party in pl:                           # 파티들을 반복문으로 돌면서
    for party_member in party:
        if party_member in know_list:
            break
    else:                                  # 파티 멤버가 한명도 아는 리스트에 없을 떄만
        ans += 1                           # +1 되도록 합니다

print(ans)