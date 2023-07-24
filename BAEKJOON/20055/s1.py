N, K = map(int, input().split())
con_belt = list(map(int, input().split()))
robot_belt = [0 for _ in range(2 * N)]

on_place, off_place = 0, N - 1

level = 0

while K > 0:
    level += 1

    on_place, off_place = (on_place - 1) % (2 * N), (off_place - 1) % (2 * N)

    if robot_belt[off_place]:
        robot_belt[off_place] = 0
        
    for n in range(N):
        i = (off_place - n) % (2 * N)
        if robot_belt[i]: 
            next_i = (i + 1) % (2 * N)
            if not robot_belt[next_i] and con_belt[next_i]:  
                robot_belt[i] = 0
                robot_belt[next_i] = 1
                con_belt[next_i] -= 1
                if con_belt[next_i] == 0:
                    K -= 1

                if next_i == off_place:
                    robot_belt[next_i] = 0

    if con_belt[on_place] and not robot_belt[on_place]:
        robot_belt[on_place] = 1
        con_belt[on_place] -= 1
            
        if con_belt[on_place] == 0:
            K -= 1

print(level)
