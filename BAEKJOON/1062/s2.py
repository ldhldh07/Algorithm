from itertools import combinations

N, K = map(int, input().split())
K -= 5

alphabet = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm','o','p','q','r','s','u','v','w','x','y','z']
word_mask = []

for _ in range(N):
    word = input().rstrip()
    mask = 0
    for char in word:
        if char in alphabet:
            mask |= (1 << alphabet.index(char))
    word_mask.append(mask)

if K < 0:
    print(0)
elif K >= 21 or N == 1:
    print(N)
else:
    max_count = 0
    for comb in combinations(range(21), K):
        mask = 0
        for c in comb:
            mask |= (1 << c)
        count = 0
        for w in word_mask:
            if w & mask == w:
                count += 1
        max_count = max(max_count, count)

    print(max_count)
