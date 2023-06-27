import sys

# 기본적으로 필요한 5개 문자를 제외한 나머지 알파벳
alphabets = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

N, K = map(int, input().split())

# 알파벳 체크
learn = [0]*26
for c in 'antic':
    learn[ord(c) - ord('a')] = 1

# 백트래킹 함수
def dfs(index, cnt):
    if cnt == K-5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        return max(answer, read_cnt) if answer else read_cnt
    for i in range(index, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, cnt + 1)
            learn[i] = 0

# 단어 받아오기
words = []
for _ in range(N):
    word = set(input().strip()[4:-4]) - set('antic')
    words.append(word)

answer = 0

# K가 5 미만이면 아무 단어도 읽을 수 없음
if K < 5:
    print(0)
# K가 26이면 모든 단어를 읽을 수 있음
elif K == 26:
    print(N)
else:
    print(dfs(0, 0))
