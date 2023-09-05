import sys

def get_unique(n):
    visited = [0 for _ in range(n+1)]
    visited[0], visited[1] = 1, 1

    for i in range(2, int(n**0.5)+1):
        if visited[i]:
            continue
        for j in range(i*i, n+1, i):
            visited[j] = 1
    
    return [x for x in range(2, n+1) if not visited[x]]
        

si = sys.stdin.readline

N = int(si().strip())

unique_until_n = get_unique(N)

start, end = -1, -1
unique_sum = 0
answer = 0

while start <= end:

    if unique_sum < N:
        if end == len(unique_until_n)-1:
            break
        end += 1
        unique_sum += unique_until_n[end]
    else:
        if start == end:
            break
        if unique_sum == N:
            answer += 1
        start += 1
        unique_sum -= unique_until_n[start]

print(answer)