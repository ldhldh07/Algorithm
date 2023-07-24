from collections import defaultdict

T = int(input())

ans_list = []

for _ in range(T):
    W = input()
    K = int(input())
    length_word = len(W)

    char_dict = defaultdict(list)
    char_count = defaultdict(int)
    max_diff = 0
    min_diff = length_word
    for index in range(length_word):
        char = W[index]
        char_dict[char].append(index)
        char_count[char] += 1

        if char_count[char] >= K:
            current_diff = index - char_dict[char][char_count[char]-K] + 1
            max_diff = max(max_diff, current_diff)
            min_diff = min(min_diff, current_diff)
    ans_list.append([min_diff, max_diff] if max_diff else 0)

for ans in ans_list:
    print(*ans) if ans else print(-1)
