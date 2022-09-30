#5356_의석이의 세로로말해요 풀이
#2022-08-16

T = int(input())

for t in range(1, 1+T):
    arr = [[''] * 5 for _ in range(15)]              # 15 * 5 의 공백문자열로 이뤄진 2차원 배열을 만듭니다.
    
    for i in range(5):                               # 5번의 입력동안 세로 가로 뒤집어진 상태로 입력이 되게 합니다.
        word = list(input())
        for j,a in enumerate(word):                  # i번째 입력의 j번째 글자를 j열 i행에 입력합니다.
            arr[j][i] = a
            
    for ii in range(15):                             # 각 줄별로 join해주고
        arr[ii] = ''.join(arr[ii])         
    print('#{} {}'.format(t, ''.join(arr)))          # 그걸 또 join 해주어서 출력해줍니다.