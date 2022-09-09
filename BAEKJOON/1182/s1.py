N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0                                # 답이 최종적으로 나올 변수입니다
for i in range(1 << N):                # N개의 원소의 부분집합의 반복문입니다
    sum_li = 0                         # 부분수열 원소의 합의 변수입니다
    len_li = 0                         # 부분수열 원소 갯수의 변수입니다
    for j in range(N):                 # 원소별로 반복해줍니다
        if i & (1 << j):               # ㅑ와 j번째 비트가 1일 때로 각 부분집합에 들어갈 원소를 구합니다
            len_li += 1                # 그 때의 원소 갯수입니다
            sum_li += arr[j]           # 원소의 합입니다
    if sum_li == S and len_li != 0:    # 부분집합의 합이 S일떄 답을 더해주되 공집합의 경우를 제외해줍니다
        ans += 1
print(ans)                             # 답을 출력해줍니다
