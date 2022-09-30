T = int(input())

for t in range(1, 1+T):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())

    ans_cnt = 0

    def sum_len(list_a):                       # 리스트의 합과 항의 수를 구하는 함수 선언
        sum_num = 0
        len_num = 0
        for n in list_a:
            sum_num += n
            len_num += 1
        return len_num, sum_num

    for i in range(1 << 12):                    # 부분집합의 수만큼 2^12 반복
        a = []                                  # 부분집합이 들어갈 변수
        for j in range(12):                     # 12개 항마다 비트 비교
            if i & (1 << j):                    # i의 j번 비트가 1이여서 요소가 들어있는지 확인
                a.append(A[j])                  # 부분집합 구성
        if sum_len(a)[0] == N and sum_len(a)[1] == K:     # 항의 수가 N이고 합이 K일때
            ans_cnt += 1                        # 하나씩 cnt 더해줌

    print('#{} {}'.format(t, ans_cnt))

