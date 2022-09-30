def binarySearchCount(N, key):                   # 이진탐색 횟수 구하는 함수
    start = 1                                    # start를 1로 하고
    end = N                                      # end를 1로 하고
    count = 0
    while start <= end :                         # start가 end 뒤로 가면 종료
        middle = int((start + end) / 2)          # 중앙값 구하기
        count += 1
        if middle == key :                       # 중앙값이 목표값이면
            return count                         # 그때의 count 반환
        elif middle > key :                      # 목표값보다 중앙값이 크면 왼쪽 절반 보기
            end = middle                         # 끝점을 중간값으로 업데이트
        else :                                   # 목표값이 중앙값보다 크면 오른쪽 절반
            start = middle

T = int(input())


for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    if binarySearchCount(P, Pa) == binarySearchCount(P, Pb):
        result = 0
    elif binarySearchCount(P, Pa) > binarySearchCount(P, Pb):
        result = 'B'
    else :
        result = "A"
                                                 # 카운트가 적은 쪽이 출력되게 설정
    print('#{} {}'.format(t, result))