import sys

si = sys.stdin.readline
p, m = map(int, si().strip().split())

game_rooms = []
entry_room = [-1 for _ in range(510)]


current_room_num = 0
for i in range(p):
    l, n = si().strip().split()

    if entry_room[l] == -1 :
        game_rooms.append([[(l, n)], m])

        for level_range in range(-10, 11):
            if l+level_range >= 0:
                entry_room[l+level_range] = current_room_num

    elif game_rooms[entry_room[l]][1] == 0:
        

    else:
        game_rooms[entry_room[l]][0].append((l, n))
        game_rooms[entry_room[l]][1] -= 1


    