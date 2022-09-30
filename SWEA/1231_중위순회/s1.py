def inorder(n):                        # 중위순회하면서 글자를 출력하는 함수입니다
    if n:                              # n이 있을 때
        inorder(ch1[n])                # 왼쪽 자식 노드 재귀호출을 먼저 합니다
        ans_list.append(word_list[n])  # 왼쪽 자식 노드에서 리턴했을 때 노드 번호를 리스트에 넣어줍니다
        inorder(ch2[n])                # 오른쪽 자식 노드 재귀호출을 합니다


T = 10

for t in range(1, T+1):

    N = int(input())                   # 정점의 갯수를 입력받습니다

    ch1 = [0] * (N + 1)                # 부모를 인덱스로 하는 왼쪽 자식 번호 배열
    ch2 = [0] * (N + 1)                # 부모를 인덱스로 하는 오른쪽 자식 번호 배열
    word_list = [0] * (N + 1)          # 인덱스 별로 글자도 배열로 만들어줍니다

    for _ in range(N):                 # 정점의 수만큼 반복문을 합니다
        arr = input().split()          # 받은 배열에서
        n = int(arr.pop(0))            # 첫번째는 해당하는 정점 번호
        word_list[n] = arr.pop(0)      # 두번째는 들어갈 글자입니다
        arr = list(map(int, arr))

        if arr:                        # 세번째가 있을 경우 왼쪽 자식 번호 리스트에
            ch1[n] = arr.pop(0)
        if arr:                        # 네번째까지 있을 경우 오른쪽 자식 번호 리스트에 넣어줍니다
            ch2[n] = arr.pop(0)

    ans_list = []
    inorder(1)                         # 루트 번호인 1을 넣고 함수를 돌려줍니다
    print('#{} {}'.format(t, ''.join(ans_list)))
