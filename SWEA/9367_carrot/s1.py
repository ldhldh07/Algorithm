import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    up_cnt = 1                             # 올라가는 수 초기값
    for a in range(1,N):                   # 두번째 값부터 반복
        if arr[a-1] < arr[a]:              # 이전값보다 크면 cnt +=1
            up_cnt += 1
        else:                              # 아니면 다시 초기화
            up_cnt = 1

    print('#{} {}'.format(t, up_cnt))