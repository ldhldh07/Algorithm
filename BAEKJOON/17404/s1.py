N = int(input())

first_R, first_G, first_B = map(int, input().split())

R_list = [first_R]
G_list = [first_G]
B_list = [first_B]

for i in range(1, N):
    R, G, B =  map(int, input().split())
    R_list.append(R)
    G_list.append(G)
    B_list.append(B)

print(R_list)
print(G_list)
print(B_list)

    # dp_R.append(min(dp_G[i-1], dp_B[i-1]) + R)
    # dp_G.append(min(dp_R[i-1], dp_B[i-1]) + G)
    # dp_B.append(min(dp_G[i-1], dp_R[i-1]) + B)



