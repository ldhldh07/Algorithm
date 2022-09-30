T = int(input())

for t in range(1, 1+T):
    N = int(input())    
    arr = [[0,1,0]]                                  # 첫번째 값 설정

    for i in range(1, N):                            # 두번째 값부터 반복문으로 추가
        arr += [[0]]                                 # 새로운 원소 추가할 겸 맨 앞 0값 넣어줍니다
        for j in range(1, i+2):                      # 앞뒤 0 넣은 것 제외 원소 반복문
            arr[i] += [arr[i-1][j-1] + arr[i-1][j]]  # 이전 원소의 두 값을 더해서 넣어줍니다
        arr[i] += [0]                                # 맨 뒤 0값 넣어줍니다.

    print('#{}'.format(t))
    for a in arr:
        for pascal in a[1:-1]:                       # 출력할 때 앞뒤 0 제거
            print(pascal, end=' ')
        print()

