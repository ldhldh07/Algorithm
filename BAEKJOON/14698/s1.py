import heapq

T = int(input())

answer = []

for t in range(T):
    slime_length = int(input())
    slime_list = list(map(int, input().split()))

    heapq.heapify(slime_list)

    cost = 1

    for _ in range(slime_length - 1):
        first_min = heapq.heappop(slime_list)
        second_min = heapq.heappop(slime_list)

        energy = first_min * second_min
        energy = (first_min * second_min) % 1000000007
        heapq.heappush(slime_list, energy)
        cost = (cost * energy) % 1000000007

    answer.append(cost)

print(*answer, sep='\n')