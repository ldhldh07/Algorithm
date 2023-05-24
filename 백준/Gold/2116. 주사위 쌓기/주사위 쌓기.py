N = int(input())
opp = [5, 3, 4, 1, 2, 0]
arr = [list(map(int, input().split())) for _ in range(N)]       # 주사위들을 배열로 받습니다
max_ans = 0
for value_top in range(1, 7):
    ans = 0
    dice_list = [a[:] for a in arr]
    for dice in dice_list:
        bottom = dice.index(value_top)
        value_top = dice[opp[bottom]]
        dice[bottom] = dice[opp[bottom]] = 0
        ans += max(dice)
    if max_ans < ans:
        max_ans = ans
print(max_ans)