N, M = map(int, input().split())

ans = N * M -1  # 한번 쪼갤때마다 조각은 하나씩 늘어나기 때문에 N*M-1만큼 쪼개면 갯수가 N*M이된다
print(ans)