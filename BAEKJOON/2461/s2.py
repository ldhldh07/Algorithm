import sys
from collections import defaultdict

si = sys.stdin.readline

N, M = map(int, si().strip().split())
students = []

for i in range(N):
    students.extend([(x, i) for x in map(int, si().strip().split())])

students.sort()

group_count = defaultdict(int)
unique_groups = set()

start, end = 0, 0
min_diff = float('inf')

while end < len(students):
    group_count[students[end][1]] += 1
    unique_groups.add(students[end][1])

    while len(unique_groups) == N:
        min_diff = min(min_diff, students[end][0] - students[start][0])

        group_count[students[start][1]] -= 1
        if group_count[students[start][1]] == 0:
            unique_groups.remove(students[start][1])

        start += 1

    end += 1

print(min_diff)