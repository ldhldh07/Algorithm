T = int(input())
for t in range(1, 1+T):
    num = float(input())
    output = ''
    for i in range(1, 13):
        a = (1/2)**i
        if num == a:
            output += '1'
            print('#{} {}'.format(t, output))
            break
        elif num > a:
            output += '1'
            num -= a
        else:
            output += '0'
    else:
        print('#{} overflow'.format(t))