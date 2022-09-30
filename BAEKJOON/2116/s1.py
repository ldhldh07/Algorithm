N = int(input())
opp = [5, 3, 4, 1, 2, 0]                                        # 반대쪽을 인덱스로 표현
arr = [list(map(int, input().split())) for _ in range(N)]       # 주사위들을 배열로 받습니다 (A~F 가 0~5에 대응됩니다)
max_ans = 0                                                     # 경우들을 돌리기 전에 최대값 변수 초기값 넣어줍니다
for value_top in range(1, 7):                                   # 위의 값을 기준으로 6가지의 경우를 돌려줍니다
    ans = 0                                                     # 각 경우별 최대값이 들어갑니다
    dice_list = [a[:] for a in arr]                             # 값을 빼면서 할것이기 때문에 배열을 깊은 복사를 해줍니다
    for dice in dice_list:                                      # 각 주사위마다
        bottom = dice.index(value_top)                          # 기본으로 이전 top값을 지금 배열에서 인덱스 찾아서 바텀 값으로 해줍니다
        value_top = dice[opp[bottom]]                           # 그 값에 따라 value_top 값을 초기화 해줍니다
        dice[bottom] = dice[opp[bottom]] = 0                    # 바닥과 윗부분을 0으로 해서 최대값에 포함되지 않도록 합니다
        ans += max(dice)                                        # 각각의 최대값을 더해줍니다
    if max_ans < ans:                                           # 그럴 때 최대값보다 크면
        max_ans = ans                                           # 최대값 갱신해줍니다
print(max_ans)