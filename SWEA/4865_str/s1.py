T = int(input())

for t in range(1, 1+T):
    str1 = input()
    str2 = input()
    max_cnt = 0

    for a in str1:
        cnt = 0
        for b in str2:
            if a == b :
                cnt += 1
        
        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(t,max_cnt))