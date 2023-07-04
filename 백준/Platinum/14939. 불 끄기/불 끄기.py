def turn_switch(i, j, light_map):
    light_map[i] = light_map[i] ^ (1 << j)

    if i-1 >= 0:
        light_map[i-1] = light_map[i-1] ^ (1 << j)
    if i+1 < 10:
        light_map[i+1] = light_map[i+1] ^ (1 << j)
    if j-1 >= 0:
        light_map[i] = light_map[i] ^ (1 << (j-1))
    if j+1 < 10:
        light_map[i] = light_map[i] ^ (1 << (j+1))

base_light_map = [int(input().replace('#', '0').replace('O', '1'), 2) for _ in range(10)]
min_switch = 101

for state in range(1 << 10): 
    cnt = 0
    temp_map = base_light_map.copy() 

    for j in range(10):
        if state & (1 << j):
            turn_switch(0, j, temp_map)
            cnt += 1

    for i in range(9):
        for j in range(10):
            if temp_map[i] & (1 << j):
                turn_switch(i+1, j, temp_map)
                cnt += 1

    if not any(temp_map):
        min_switch = min(min_switch, cnt)

if min_switch == 101:
    print(-1)
else:
    print(min_switch)