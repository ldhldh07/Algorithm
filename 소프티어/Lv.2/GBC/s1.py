N, M = map(int, input().split())

limit_start = 0
section_limit = []

for _ in range(N):
    limit_length, limit = map(int, input().split())
    limit_start += limit_length
    section_limit.append((limit_start, limit))

check_end = 0
current_section = 0
max_diff = 0

for _ in range(M):
    check_length, speed = map(int, input().split())
    check_end += check_length

    while True:
        limit_start, limit =  section_limit[current_section]
        max_diff = max(max_diff, speed-limit)
        if limit_start < check_end:
            current_section += 1
        elif limit_start == check_end:
            current_section += 1
            break
        else:
            break

print(max_diff)
