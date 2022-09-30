num_list = []

for n in range(10 ** 6 + 1):                # 범위 내에서 가장 큰 세제곱근이 10**6이기 때문에 여기까지만 탐색합니다
    num_list.append(n ** 3)                 # 세제곱근이 들어간 리스트를 만듭니다ㅏ

T = int(input())
for t in range(1, 1 + T):
    N = int(input())
    for i, a in enumerate(num_list):
        if N == a:                          # 리스트에 있으면 출력해줍니다
            print('#{} {}'.format(t, i))
            break                           # 반복문 끝내줍니다
        elif N < a:                         # 리스트에 있는 수가 더 커졌으면 멈춥니다
            print('#{} {}'.format(t, -1))
            break
