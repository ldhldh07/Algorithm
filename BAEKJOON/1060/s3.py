import heapq

L = int(input().strip())
S = sorted(list(map(int, input().strip().split())))
N = int(input().strip())

segments = [(S[i]-S[i-1]-1, S[i-1]+1, S[i]-1) for i in range(1, L)]
segments.append((S[0]-1, 1, S[0]-1))
segments.append((10**9 - S[-1], S[-1]+1, 10**9))

heapq.heapify(segments)

res = []

while len(res) < N:
    length, start, end = heapq.heappop(segments)
    mid = (start+end) // 2
    res.append(mid)
    
    if mid-1 >= start:
        heapq.heappush(segments, (mid-1-start+1, start, mid-1))
    if mid+1 <= end:
        heapq.heappush(segments, (end-mid, mid+1, end))

print(*sorted(res))
