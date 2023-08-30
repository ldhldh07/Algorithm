import sys
from collections import deque

def topology_sort(indegree, adjs, n):
    result = [-1 for _ in range(n)]
    queue = deque()
    for i in range(n):
        if not indegree[i]:
            queue.append(i)
    while queue:
        node = queue.popleft()
        
        if result[node] != -1:
            continue
        
        result[node] = 1
        next_node = adjs[node]
        result[next_node] = 0
        
        next_next_node = adjs[next_node]
        indegree[next_next_node] -= 1
        if not indegree[next_next_node]:
            queue.append(next_next_node)

    for j in range(n):
        if result[j] == -1:
            check_cycle(j, result, adjs, n)
        
    return result


def check_cycle(i, result, adjs, n):
    visited = [0 for _ in range(n)]
    current_node = i
    state = -1
    cycle_list = []
    while True:
        if visited[current_node]:
            return False
        if result[current_node] != -1:
            if state == -1:
                state = result[current_node]
            else:
                if state != result[current_node]:
                    return False
        cycle_list.append(current_node)
        next_node = adjs[current_node]
        if next_node == i:
            set_cycle(cycle_list, result)
            return True
        current_node = next_node


def set_cycle(cycle_list, result):
    len_cycle = len(cycle_list)
    start_i = 0
    start_state = 0
    for i in range(len_cycle):
        i_index = cycle_list[i]
        if result[i_index] != -1:
            start_i = i
            start_state = result[i_index]
    
    for j in range(len_cycle):
        result[cycle_list[j]] = 1 - start_state if abs(j-start_i) % 2 else start_state    


si = sys.stdin.readline

m, n = map(int, si().strip().split())
students = list(map(int, si().strip().split())) +  list(map(int, si().strip().split()))
indegree = [0 for _ in range(m+n)]
adj_list = {}
for i in range(m + n):
    face_student = students[i]
    if i < m:
        adj_list[i] = face_student + m - 1
        indegree[m + face_student - 1] += 1
    else:
        adj_list[i] = face_student - 1
        indegree[face_student - 1] += 1


result = topology_sort(indegree, adj_list, n + m)

print(*result[:m], sep='')
print(*result[m:m+n], sep='')