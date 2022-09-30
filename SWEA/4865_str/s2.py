T = int(input())

for t in range(1, 1+T):

    str1 = input()
    str2 = input()
    str_dict = {}                   # str1의 글자들로 구성된 딕셔너리 만듭니다
    max_cnt = 0

    for a in str1:                  # a의 글자들이 key값으로 들어갑니다
        str_dict[a] = 0
    
    for b in str2:                  # b에 그 글자들이 있을 때 value +=1 해줍니다.
        if b in str_dict :
            str_dict[b] += 1

    for c in str_dict.values():     # value값 중 최대값 구해줍니다.
        if max_cnt < c:
            max_cnt = c

    print('#{} {}'.format(t,max_cnt))