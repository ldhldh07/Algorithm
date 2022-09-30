# 4834_숫자카드
# 2022-08-09

T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    num_list = input()
    cnt_dict = {}                                  # 숫자와 그 갯수로 이뤄진 dict 생성
    max_count = 0
    num_ans = list(num_list)[0]

    for num in num_list:                           # 숫자가 key로 없으면
        if num not in cnt_dict:                    # value를 1로 key값 추가
            cnt_dict[num] = 1
        else :                                     # 있으면
            cnt_dict[num] += 1                     # value값 1 추가
    
    for n, cnt in cnt_dict.items() :               # 딕셔너리 반복문
        if max_count < cnt:                        # 최대값 설정
            max_count = cnt
            num_ans = n                            # 그때의 숫자값 결과값에 배정
        elif max_count == cnt and n > num_ans:     # 최대갯수 가진 수중에서는 더 큰값
            num_ans = n

    print('#{} {} {}'.format(t, num_ans, max_count))