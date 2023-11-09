import heapq

def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)

    for _ in range(n):
        if works[0] == 0:
            break
        heapq.heappush(works, heapq.heappop(works) + 1)

    return sum(x*x for x in works)