N = int(input())
# 3개의 DP배열을 만드는 방식
R, G, B = map(int, input().split())

# 마지막이 각각 R, G, B일때의 최솟값을 각 배열에 넣습니다
dp_R = [R]
dp_G = [G]
dp_B = [B]

# 이전 순서에 다른 색이 나온 두 경우의 dp최솟값에서 해당 순서의 색깔 비용을 더해줍니다
for i in range(1, N):
    R, G, B = map(int, input().split())
    dp_R.append(min(dp_G[i-1], dp_B[i-1])+R)
    dp_G.append(min(dp_R[i-1], dp_B[i-1])+G)
    dp_B.append(min(dp_G[i-1], dp_R[i-1])+B)
# 3가지 색깔 최솟값 중에 또 최솟값을 구해서 출력합니다.
print(min(dp_R.pop(),dp_G.pop(),dp_B.pop()))

# 30840KB 108ms