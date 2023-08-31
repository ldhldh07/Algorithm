import sys, heapq
from collections import defaultdict

si = sys.stdin.readline

N = int(si().strip())
problems = defaultdict(list)

for i in range(N):
    deadline, cupramyun = map(int, si().strip().split())    
    problems[deadline].append(cupramyun)

max_deadline = max(problems.keys())

queue = []
answer = 0

for timing in range(max_deadline, 0, -1):
    for timing_cupramyun in problems[timing]:
        heapq.heappush(queue, -timing_cupramyun)
    if queue:
        answer += -heapq.heappop(queue)

print(answer)