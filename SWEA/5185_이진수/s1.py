T = int(input())
a = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for t in range(1, 1+T):

    N, bin_num = input().split()
    N = int(N)

    output = ''
    for n in bin_num:

        if n in a:                  # 16진수중 알파벳을 쓰는 단어들 변환
            b = a[n]
        else:
            b = int(n)

        for c in range(3, -1, -1):   # 2진수 형식으로 변환하며 이전 답과도 이어서 출력
            output += "1" if b & (1 << c) else "0"

    print('#{} {}'.format(t, output))

