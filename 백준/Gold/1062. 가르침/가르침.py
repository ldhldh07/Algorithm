N, K = map(int, input().split())

learn = [0]*26

for char in 'antic':
    learn[ord(char) - ord('a')] = 1

def dfs(index, cnt, k):
    global max_reading_word
    if cnt == k:
        reading_word = 0
        for word in words:
            for char in word:
                if not learn[ord(char) - ord('a')]:
                    break
            else:
                reading_word += 1
        max_reading_word = max(max_reading_word, reading_word)
        return
    for next_index in range(index, 26):
        if not learn[next_index]:
            learn[next_index] = 1
            dfs(next_index, cnt + 1, K)
            learn[next_index] = 0

words = []
for _ in range(N):
    word = set(input()[4:-4]) - set('antic')
    words.append(word)

max_reading_word = 0

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    dfs(0, 5, K)
    print(max_reading_word)