from itertools import combinations

def distance(start_i, start_j, end_i, end_j):
    distance_i = start_i - end_i if start_i > end_i else end_i - start_i
    distance_j = start_j - end_j if start_j > end_j else end_j - start_j
    return distance_i + distance_j


def search_city_chicken_distance(start_list, end_list):
    city_chicken_distance = 0
    for start_i, start_j in start_list:
        chicken_distance = 2 * (N - 1)
        for end_i, end_j in end_list:
            current_ditsance = distance(start_i, start_j, end_i, end_j)
            if chicken_distance > current_ditsance:
                chicken_distance = current_ditsance
        city_chicken_distance += chicken_distance
    return city_chicken_distance


N, M = map(int, input().split())

home_list = []
chicken_list = []
array = []

for j in range(N):
    arr = list(map(int, input().split()))
    for i in range(N):
        if arr[i] == 1:
            home_list.append((i,j))
        if arr[i] == 2:
            chicken_list.append((i,j))
    array.append(arr)

new_chicken_list_list = combinations(chicken_list, M)
min_chicken_distance = N * N * 2 * (N-1)
for new_chicken_list in new_chicken_list_list:
    current_chicken_distance = search_city_chicken_distance(home_list, new_chicken_list)
    if current_chicken_distance < min_chicken_distance:
        min_chicken_distance = current_chicken_distance
print(min_chicken_distance)