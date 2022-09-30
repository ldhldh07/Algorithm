T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    num_list = input().split()

    def sum_m(list_a, idx, length):                                                # 리스트에서 연속된 M개 합 구하는 함수 선언
        s = 0
        for ii in range(length):                                                   # 해당 수부터 length만큼 반복해서 뒤로 가면서 합
            s += int(list_a[idx + ii])
        return s
  
    max_ans = sum_m(num_list, 0, M) - sum_m(num_list, 1, M)                        # M개 합 두 묶음의 최대 차이

    for idx_a in range(N-M+1) :
        for idx_b in range(N-M+1) :
            if sum_m(num_list, idx_a, M)-sum_m(num_list, idx_b, M) > max_ans :     # 최대 차이가 들어가도록 설정
                max_ans = sum_m(num_list, idx_a, M)-sum_m(num_list, idx_b, M)

    print('#{} {}'.format(t, max_ans))
