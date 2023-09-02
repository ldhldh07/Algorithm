import sys, heapq
from collections import defaultdict

si = sys.stdin.readline

N = int(si().strip())
problems = defaultdict(list)

for _ in range(N):
    deadline, cupramyun = map(int, si().strip().split())    
    problems[deadline].append(cupramyun)

max_deadline = max(problems.keys())

priority_queue = []
answer = 0

for timing in range(max_deadline, 0, -1):
    for cupramyuns in problems[timing]:
        heapq.heappush(priority_queue, -cupramyuns)
    if priority_queue:
        answer -= heapq.heappop(priority_queue)

print(answer)