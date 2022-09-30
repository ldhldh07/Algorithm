T = 10
for _ in range(1, 1+T):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    for a in arr:                             # 행의 합 반복문으로 돌려서 최대값
        row_sum = 0
        for b in a:
            row_sum += b
        if row_sum >=max_sum :
            max_sum = row_sum

    for b in range(100):                       # 열의 합 반복문으로 돌려서 최대값
        column_sum = 0
        for c in range(100):
            column_sum += arr[c][b]
        if column_sum >= max_sum:
            max_sum = column_sum

    dig_a_sum = 0                               # 대각선1의 합과 최대값 비교
    for d in range(100):
        dig_a_sum += arr[d][d]
    if dig_a_sum >=max_sum:
        max_sum = dig_a_sum

    dig_b_sum = 0                               # 대각선2의 합과 최대값 비교
    for e in range(100):
        dig_b_sum += arr[e][99-e]
    if dig_b_sum >= max_sum:
        max_sum = dig_b_sum

    print('#{} {}'.format(tc, max_sum))         # 최종 최대값 출력


