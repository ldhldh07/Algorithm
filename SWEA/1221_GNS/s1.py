
T = int(input())
str_num = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
                                                    # 딕셔너리에 문자에 숫자 넣어주기
for _ in range(1, 1+T):
    N = input().split()
    tc = N[0]
    N2 = int(N[1])
    arr = list(input().split())
                                                     # 딕셔너리 value값 기준으로 버블정렬
    for i in range(N2-1, 0, -1):                     # 마지막 값부터 왼쪽으로
        for j in range(0, i):                        # 첫번째 값부터 i-1값까지
            if str_num[arr[j]] > str_num[arr[j+1]]:  # 더 큰값 오른쪽으로 반복
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(tc)
    print(' '.join(arr))  