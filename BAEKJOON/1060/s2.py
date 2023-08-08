import sys, heapq

def get_count_good(length, i):
    return i * (length - i) - 1

L = int(input().strip())
S = sorted(list(map(int, input().strip().split())))
N = int(input().strip())

priority_queue = []
length_list = [0 for _ in range(L)]
prev_num = 0

for i, num in enumerate(S):
    length = num - prev_num
    length_list[i] = length
    prev_num = num

search_index = [0 for _ in range(L)]


ans_list = []

for section_i in range(L):
    if length_list[section_i] > 1: 
        heapq.heappush(priority_queue, (
            get_count_good(length_list[section_i], 1),
            [(0 if not section_i else S[section_i-1]) + 1,  S[section_i]-1],
            section_i
        ))
        ans_list.append(S[section_i])
        N -= 1
        if not N:
            break

print(ans_list)
print(priority_queue)


while priority_queue and N > 0: 
    _, answer, current_section_i = heapq.heappop(priority_queue)
    ans_list.append(answer[0])
    N -= 1
    if not N:
        break
    if answer[0] != answer[1]:
        ans_list.append(answer[1])
        N -= 1
        if not N:
            break

    current_search_i = search_index[current_section_i]
    current_length = length_list[current_section_i]

    if current_search_i > (current_length) // 2 - 1:
        continue

    current_search_i += 1
    search_index[current_section_i] = current_search_i
    heapq.heappush(priority_queue, (
        get_count_good(current_length, current_search_i),
        [(0 if not current_section_i else S[current_section_i-1]) + current_search_i, S[current_section_i]-current_search_i],
        current_section_i
    ))

infinity_count = S[-1] + 1

while N > 0:
    ans_list.append(infinity_count)
    infinity_count += 1
    N -= 1

print(*ans_list, sep=" ")
