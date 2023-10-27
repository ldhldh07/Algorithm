import sys
from collections import defaultdict

def get_diff(i, j):
    return students[j][0] - students[i][0]

si = sys.stdin.readline

N, M = map(int, si().strip().split())

students = []
for i in range(N):
    students.extend([(x, i) for x in map(int, si().strip().split())])

students.sort()

answer = 0

group_count = defaultdict(int)
unique_groups = set()

start, end = 0, len(students) - 1
min_diff = float('inf')

while start < end:
    diff = get_diff(start, end)

    if diff < min_diff and len(unique_groups) == N:
        min_diff = diff

    if get_diff(start+1, end) < get_diff(start, end-1):
        group_count[students[start][1]] -= 1
        if not group_count[students[start][1]]:
            unique_groups.remove(students[start][1])
        start += 1
    else:
        group_count[students[end][1]] += 1
        unique_groups.add(students[end][1])
        end -= 1

print(min_diff)