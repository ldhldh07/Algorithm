T = int(input())

def row_pal(arr_a, n, l):                             # n*n 이차원 배열에서 가로 l길이의 회문을 구하는 함수
    result=''
    for i in range(n):
        for j in range(n-l+1):                        # 끝 넘어가지 않는 인덱스 범위 설정
            row_word = arr_a[i][j:j+l]                # l길이만큼 슬라이싱했을때
            if row_word == row_word[::-1]:            # 회문이 되면 
                result = row_word                     # row_word 변수에 넣습니다
    return result


for t in range(1, 1+T):
    N, M = map(int,input().split())

    arr = [input() for _ in range(N)]
    arr_rev = [[0] * N for _ in range(N)]             # arr을 가로세로 뒤집는 이차원 배열 제작        


    for ii in range(N):                               # 뒤집은값을 리스트로 넣은 후에
        for jj in range(N):
            arr_rev[ii][jj] = arr[jj][ii]
    
    for iii in range(N):                              # join으로 arr과 같은 형태로 만듭니다
        arr_rev[iii] = ''.join(arr_rev[iii])

    ans = row_pal(arr, N, M) + row_pal(arr_rev, N, M) # 두개 다 가로로 된 회문 구하는 함수에 돌리고 
                                                      # 답은 하나라고 했으니 더해서 있는 값만 나오도록 합니다.
    print('#{} {}'.format(t, ans))                    # ans 출력