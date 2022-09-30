T = int(input())

for t in range(1, 1+T):
    N, P = map(int, input().split())  # N을 가장 균등하게 나눴을 때 곱하기 값이 가장 큼
    a = N // P                        # 균등한 값은 나눈 몫(a)에 가깝기 때문에 N을 P로 나눈 값을 구하고
    b = N % P                         # 남은 값은 P개로 나눠져 있는 몫(a)들에 1씩 나눠줄 때 균등하게 나눠짐
    ans = ((a+1) ** b) * (a ** (P-b)) # 그러면 분할값 P개중 a+1인 값이 나머지 갯수(b)만큼 있고 나머지(P-b)개는는 a가 됨
    print('#{} {}'.format(t, ans))