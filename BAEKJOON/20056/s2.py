from collections import defaultdict

delta = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1)
]

def shark_order(n, arr):
    new_arr = defaultdict(list)
    for (i, j), sharks in arr.items():
        for weight, speed, direction in sharks:
            delta_i, delta_j = delta[direction]
            next_i, next_j = (i + speed * delta_i) % n, (j + speed * delta_j) % n
            new_arr[(next_i, next_j)].append((weight, speed, direction))

    for (new_i, new_j), fire_ball_list in new_arr.items():
        fire_ball_length = len(fire_ball_list)
        if fire_ball_length > 1:
            direction_state = 0
            for index, fire_ball in enumerate(fire_ball_list):
                current_weight, current_speed, current_direction = fire_ball
                if not index:
                    sum_weight = current_weight
                    sum_speed = current_speed
                    prev_direction_odd = current_direction % 2
                else:
                    sum_weight += current_weight
                    sum_speed += current_speed
                    if not direction_state and prev_direction_odd != current_direction % 2:
                        direction_state = 1
            new_weight = sum_weight // 5
            new_speed = sum_speed // fire_ball_length
            new_balls = [] 
            if new_weight:
                for i in range(4):
                    new_balls.append((new_weight, new_speed, i * 2 + direction_state))
            new_arr[(new_i, new_j)] = new_balls
    return new_arr


                
N, M, K = map(int, input().split())
array = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    array[(r, c)].append((m, s, d))

for _ in range(K):
    array = shark_order(N, array)
ans = 0

for ball_list in array.values():
    for w, d, s in ball_list:
        ans += w
print(ans)
