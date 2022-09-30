T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [0] * 5000                            # 정류장별 멈춘 횟수를 모으는 배열을 만들어줍니다

    for _ in range(N):                          # 노선마다
        A, B = list(map(int, input().split()))

        for stop_station in range(A, B+1):      # A에서 B까지 정류장을 거치면서
            arr[stop_station-1] += 1            # 정류장마다 +1 해줍니다

    print('#{}'.format(t), end=' ')

    P = int(input())                            # 몇개의 답을 구할지 입력받습니다
    ans_list = []                               # 리스트 만들어줍니다

    for _ in range(P):
        C = int(input())
        ans_list.append(str(arr[C-1]))          # 멈춘 횟수로 만든 배열에서 인덱스로 찾아줍니다

    print(' '.join(ans_list))