import sys

def get_length(index, n):
    temp = 2 * index - 1
    if index <= (n+1) // 2:
        return temp * (temp+1) // 2
    else:
        return n ** 2 - (2 * (n-index)) * (2 * (n-index) + 1) // 2


def make_list(i, n):
    result = []
    for s in [2 * i - 1, 2 * i]:
        for u in range(max(1, s-n), s//2 + 1):
            result.append(u * (s - u))
            if not u * 2 == s:
                result.append(u * (s - u))
                
    return result


si = sys.stdin.readline

N, K = int(si().strip()), int(si().strip())

for i in range(N+1):
    current_length = get_length(i, N)
    if current_length >= K:
        section = i
        index = K - prev_length - 1
        break
    prev_length = current_length

print(sorted(make_list(section, N))[index])