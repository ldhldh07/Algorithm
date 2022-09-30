shift = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


def code_solve(a):
    output = []
    len_output = 0
    for b in a:
        c = int('0x' + b, 16)
        for n in range(3, -1, -1):
            output.append('1' if c & (1 << n) else '0')
            len_output += 1
    final_output = []
    len_final_output = (len_output // 56) * 56
    for i in range(len_output-1, -1, -1):
        if output[i] != '0':
            for j in range(i-len_final_output+1, i+1):
                final_output.append(output[j])
            break
    num_cnt = len_final_output // 56
    sum1 = 0
    sum2 = 0
    for aa in range(8):  # 0,1,2,3,4,5,6,7
        num_code = ''
        for bb in range(0, 7 * num_cnt, num_cnt):
            num_code += final_output[7 * num_cnt * aa + bb]
        if aa % 2:
            sum2 += shift[num_code]
        else:
            sum1 += shift[num_code]
    if (sum1*3 + sum2) % 10:
        return 0
    else:
        return sum1 + sum2


T = int(input())

for t in range(1, 1+T):
    N, M = map(int, input().split())
    code_list = []
    for _ in range(N):
        arr = list(input())
        code = []
        for m in range(M):
            if code and arr[m] == '0':
                if code not in code_list:
                    code_list.append(code)
                code = []
            elif arr[m] != '0':
                code.append(arr[m])
    ans = 0
    for codes in code_list:
        ans += code_solve(codes)
    print('#{} {}'.format(t, ans))