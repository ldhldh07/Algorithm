def inorder_calc(n):               # 좌측 노드와 우측 노드를 계산하는 함수를 만듭니다
    calc_arr = arr_list[n]         # 해당 노드의 입력 리스트를 가져옵니다
    if calc_arr[1] == '+':         # 각각 기호별로 좌측 우측에서 재귀호출한 값을 계산해줍니다
        return inorder_calc(int(calc_arr[2])) + inorder_calc(int(calc_arr[3]))
    elif calc_arr[1] == '-':
        return inorder_calc(int(calc_arr[2])) - inorder_calc(int(calc_arr[3]))
    elif calc_arr[1] == '*':
        return inorder_calc(int(calc_arr[2])) * inorder_calc(int(calc_arr[3]))
    elif calc_arr[1] == '/':
        return inorder_calc(int(calc_arr[2])) / inorder_calc(int(calc_arr[3]))
    else:                           # 리스트의 두번째 값이 기호가 아닐경우 리프 노드이므로
        return int(calc_arr[1])     # 그 값을 그대로 호출시킵니다


T = 10

for t in range(1, 1+T):

    N = int(input())
    arr_list = [0] * 1000
    for i in range(1, N + 1):
        arr = list(input().split())
        arr_list[i] = arr           # 노드별 리스트를 또다시 리스트에 담아줍니다.

    print('#{} {}'.format(t, int(inorder_calc(1))))

