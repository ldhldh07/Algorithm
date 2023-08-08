import sys

si = sys.stdin.readline

N = int(si().strip())

offers = []

for consumer in range(N):
    A, *query = map(int, si().split())
    for i in range(A):
        car_size, offer = query[i * 2], query[2 * i + 1]
        offers.append((car_size, offer, consumer))

M = int(si().strip())

scenarios = list(enumerate(map(int, si().strip().split())))

offers.sort()
scenarios.sort(key = lambda scenario : scenario[1])

consumer_max_offer = [0 for _ in range(N)]
revenue = 0
scenario_index = 0
current_scenario = scenarios[0][1]

ans = [-1 for _ in range(M)]

for car_size, offer, consumer in offers:
    if offer > consumer_max_offer[consumer]:
        prev_max_offer = consumer_max_offer[consumer]
        revenue += -prev_max_offer + offer
        consumer_max_offer[consumer] = offer
    while scenario_index < M and current_scenario <= revenue:
        ans[scenarios[scenario_index][0]] = car_size
        scenario_index += 1
        current_scenario = scenarios[scenario_index][1]

print(*ans, sep=' ')