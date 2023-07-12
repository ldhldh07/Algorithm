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
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                for weight, speed, direction in arr[i][j]:
                    delta_i, delta_j = delta[direction]
                    next_i, next_j = (i + speed * delta_i) % n, (j + speed * delta_j) % n
                    new_arr[next_i][next_j].append((weight, speed, direction))
    
    for new_i in range(n):
        for new_j in range(n):
            fire_ball_length = len(new_arr[new_i][new_j])
            if fire_ball_length > 1:
                direction_state = 0
                for index, fire_ball in enumerate(new_arr[new_i][new_j]):
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
                new_arr[new_i][new_j] = new_balls
    return new_arr


                
N, M, K = map(int, input().split())
array = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    array[r-1][c-1].append((m, s, d))

for _ in range(K):
    array = shark_order(N, array)
ans = 0

for i in range(N):
    for j in range(N):
        if array[i][j]:
            for w, d, s in array[i][j]:
                ans += w
print(ans)