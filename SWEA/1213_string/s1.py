
def lenlen (a):                                 # 글자수 세는 함수
    len_a = 0
    for _ in a:
        len_a += 1
    return len_a

T = 10

for _ in range(1, T+1):
    t = input()
    str_a = input()
    str_b = input()

    eq_count = 0                                # 같은 문자열 갯수 초기값

    for i in range(len(str_b)-len(str_a)+1):    # 마지막에 찾는 문자열 맨앞문자까지만 해당되게 범위 설정
        if str_a == str_b[i:i+len(str_a)]:      # 전체에서 슬라이싱한 값이 찾는 문자열과 같을 때
            eq_count += 1                       # count +1

    print('#{} {}'.format(t, eq_count))