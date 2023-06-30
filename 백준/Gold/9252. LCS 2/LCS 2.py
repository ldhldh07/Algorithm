first_word = input()
second_word = input()

first_word_length = len(first_word)
second_word_length = len(second_word)

dp = [[[0, ''] for _ in range(first_word_length + 1)] for _ in range(second_word_length + 1)]

for i in range(1, second_word_length + 1):
    for j in range(1, first_word_length + 1):
        if first_word[j-1] == second_word[i-1]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = dp[i-1][j-1][1] + first_word[j-1]
        else:
            if dp[i-1][j][0] >= dp[i][j-1][0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = dp[i][j-1][1]

print(dp[i][j][0])
print(dp[i][j][1])