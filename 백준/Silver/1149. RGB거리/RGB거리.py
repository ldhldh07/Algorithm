N = int(input())

R, G, B = map(int, input().split())

dp_R = [R]
dp_G = [G]
dp_B = [B]


for i in range(1, N):
    R, G, B = map(int, input().split())
    dp_R.append(min(dp_G[i-1], dp_B[i-1])+R)
    dp_G.append(min(dp_R[i-1], dp_B[i-1])+G)
    dp_B.append(min(dp_G[i-1], dp_R[i-1])+B)

print(min(dp_R.pop(),dp_G.pop(),dp_B.pop()))