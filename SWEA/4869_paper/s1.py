T = int(input())

for t in range(1, T+1):
    N = int(input()) // 10                                  # 10으로 나눈 값을 구해줍니다
    ans_list = [1, 3]                                       # 10, 20짜리 만드는 경우의 수입니다
    for i in range(2, N):                                   # 30부터 구해줍니다
        ans_list.append(ans_list[i-2] * 2 + ans_list[i-1])  # 10 더 작은 종이에서 10짜리 붙일 수있고
                                                            # 20 더 작은 종이에서 20이랑 가로 10 2개 붙일 수 있어서 계산해줍니다
    print('#{} {}'.format(t, ans_list[N-1]))