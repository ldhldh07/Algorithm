T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))        # 배열을 입력받습니다
    heap = [0] * (N + 1)                         # 힙 배열을 만듭니다
    last = 0                                     # 마지막 인덱스를 기록합니다
    for a in arr:                                # 입력받은 배열을 앞에서부터 넣습니다
        last += 1                                # last인덱스에 입력값을 넣어줍니다
        heap[last] = a
        c = last                                 # 자식노드로 현재 넣은걸 지정하고
        p = c // 2                               # 부모노드는 2로 나눈 몫으로 따집니다
        while heap[p] > heap[c]:                 # 부모노드가 자식 노드보다 작아질때까지
            heap[p], heap[c] = heap[c], heap[p]  # 두개를 바꿔줍니다
            c = p                                # 바꾼경우 부모, 자식을 재설정해줍니다
            p = c // 2

    ans = 0

    while last != 1:                             # 마지막 값에서부터 루트 노드까지
        last = last // 2                         # 부모를 계속 찾아가면서
        ans += heap[last]                        # 값을 더해갑니다

    print('#{} {}'.format(t,ans))