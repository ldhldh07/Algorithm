from collections import defaultdict

T = int(input())

ans_list = []

for _ in range(T):
    W = input()
    K = int(input())
    length_word = len(W)

    char_dict = defaultdict(list)
    char_count = defaultdict(int)
    max_diff = -1
    min_diff = float('inf')

    for index in range(length_word):
        char = W[index]
        char_dict[char].append(index)
        char_count[char] += 1

        if char_count[char] < K:
            continue
        else:
            start_index = char_dict[char][char_count[char]-K]
            end_index = char_dict[char][-1]
            if W[start_index] == W[end_index]:
                max_diff = max(max_diff, end_index - start_index + 1)
            min_diff = min(min_diff, end_index - start_index + 1)

    ans_list.append([min_diff, max_diff] if max_diff != -1 else -1)

for ans in ans_list:
    print(*ans) if ans != -1 else print(-1)