first_word, second_word, third_word = [input() for _ in range(3)]
first_word_length, second_word_length, third_word_length = len(first_word), len(second_word), len(third_word)
dp = [[[0 for _ in range(third_word_length+1)] for _ in range(second_word_length+1)] for _ in range(first_word_length+1)]

for i in range(1, 1+first_word_length):
    for j in range(1, 1+second_word_length):
        for w in range(1, 1+third_word_length):
            if first_word[i-1] == second_word[j-1] == third_word[w-1]:
                dp[i][j][w] = dp[i-1][j-1][w-1] + 1
            else:
                dp[i][j][w] = max(dp[i-1][j][w], dp[i][j-1][w], dp[i][j][w-1])

print(dp[i][j][w])