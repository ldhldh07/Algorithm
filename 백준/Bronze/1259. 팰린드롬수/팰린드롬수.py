while True:
    N = input()
    if N == '0':
        break
    else:
        w = ''
        for a in N:
            w = a + w
        if w == N:
            print('yes')
        else:
            print('no')