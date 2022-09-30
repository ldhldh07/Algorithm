# 1974_sudoku 풀이
# 2022-08-19

T = int(input())

def chk(nine):                                             # 숫자 9개가 성립하는지 확인하는 함수를 만듭니다
    num_dict = {1:0, 2:0, 3:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for num in nine:                                       # 딕셔너리에 숫자를 더해서
        num = int(num)
        num_dict[num] += 1
    if 0 in num_dict.values():                             # value가 0인 값이 있으면 0을 return합니다
        return 0
    else:
        return 1

for t in range(1, T+1):

    p_list = [''.join(input().split()) for _ in range(9)]  # 가로 9개씩 묶인 문자열의 리스트입니다
    y_list = [''] * 9                                      # 세로 9개씩 묶인 문자열의 리스트입니다
    g_list = []                                            # 9분할 상자에 들어있는 문자열의 리스트입니다.

    for i in range(9):                                     # 세로 9개씩 묶기 위해
        for j in range(9):
            y_list[j] += p_list[i][j]                      # [j]번째 항에 i열 j행 숫자가 더해지도록 합니다

    for g in range(9):                                     # 9분할 상자 문자열을 구하기 위해
        num_list = ''
        for ii in range((g // 3) * 3, (g // 3) * 3 + 3):   # 3x3상자 위치를 i, j를 3으로 나눈 몫, 나머지를 이용합니다
            for jj in range((g % 3) * 3, (g % 3) * 3 + 3):
                num_list += p_list[ii][jj]
        g_list.append(num_list)

    all_list = p_list + y_list + g_list                    # 27개의 문자열을 다 합칩니다

    result = 1                                             # result 기본값을 1로 두고
    for nine_num in all_list:                              # 문자열중 스도쿠 체크가 0이 나오면
        if chk(nine_num) = 1:
            result = 0                                     # result를 0으로 바꿔줍니다

    print('#{} {}'.format(t, result))