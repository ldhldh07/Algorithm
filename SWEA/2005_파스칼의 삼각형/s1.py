T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [[0] * (n+3) for n in range(N)]            # 기존의 모양에 앞뒤에 0 하나씩 추가한 2차원 배열 제작
    arr[0][1] = 1                                    # 첫번째 열의 1 값 추가

    for a in range(1, N):                            # 2번째 열부터 적용
        for b in range(1,a+2):                       # 앞뒤 0 넣은 것 제외 원소 반복문
            arr[a][b] = arr[a-1][b-1] + arr[a-1][b]  # 이전 열의 b-1, b번째 원소 더해서 넣기

    print('#{}'.format(t))
    for a in arr:
        for b in a[1:-1]:                            # 출력할 때 넣었던 0 제거
            print(b, end=' ')
        print()

