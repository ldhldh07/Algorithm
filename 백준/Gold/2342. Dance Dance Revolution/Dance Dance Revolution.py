def move_energy(start, end):
    if start == end:
        return 1
    elif start == 0:
        return 2
    elif abs(start - end) == 2:
        return 4
    else:
        return 3

ddr_list = list(map(int, input().split()))
ddr_list = ddr_list[:-1]
length_ddr = len(ddr_list)
max_energy = 4 * 10 ** 5
dp = [[[max_energy for _ in range(5)] for _ in range(5)] for _ in range(length_ddr+1)]
dp[0][0][0] = 0

for index in range(1, length_ddr+1):
    current_ddr = ddr_list[index-1]
    for left_foot in range(5):
        for right_foot in range(5):
            if left_foot == current_ddr:
                for other_foot in range(5):
                    dp[index][left_foot][right_foot] = min(dp[index][left_foot][right_foot], dp[index-1][other_foot][right_foot] + move_energy(other_foot, left_foot))
            if right_foot == current_ddr:
                for other_foot in range(5):
                    dp[index][left_foot][right_foot] = min(dp[index][left_foot][right_foot], dp[index-1][left_foot][other_foot] + move_energy(other_foot, right_foot))

print(min(min(dp[length_ddr][left][right] for left in range(5)) for right in range(5)))