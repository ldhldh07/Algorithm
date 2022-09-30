
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):                                  # 마지막 교환은 안해도 되므로 N-1만큼 반복
        if i % 2:                                         # i가 홀수일때는 최솟값 맨 앞으로 이동
            min_idx = i                                   # 맨 앞의 값 i로 초기값 설정
            for j in range(i+1, N):                       # i 뒤의 값부터 마지막까지 반복
                if arr[min_idx] > arr[j] :                # 최솟값의 인덱스값이 min_idx에 들어가도록
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]   # i에 있는 값과 min_idx에 있는 값 교환
        else:                                             # i가 짝수일때
            max_idx = i
            for j in range(i+1, N):
                if arr[max_idx] < arr[j]:                 # 최대값이 맨 앞으로 가게
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]


    print('#{} '.format(t), end='')
    for n in arr[:10]:
        print(n, end=' ')
    print()