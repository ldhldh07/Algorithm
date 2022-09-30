def my_len(my_list):                              # len 역할 하는 함수 선언
    lenlen = 0
    for _ in my_list:
        lenlen += 1
    return lenlen

T = int(input())

for t in range(1, T+1):
    A, B = map(list,input().split())              # 이후 글자 제거 용이하게 리스트로 변환

    b_count = 0                                   # B가 몇번 들어가는지 카운트
    
    for a in range(my_len(A)-my_len(B)+1):        # A를 B단어갯수만큼 슬라이싱해서 반복
        if A[a:a+my_len(B)] == B :                # 슬라이싱한 단어가 B와 같으면
            b_count +=1                           # b_count 누적하고
            A[a:a+my_len(B)] = [''] * my_len(B)   # 해당 단어는 공백칸으로 바꿔준다
                         

    ans = my_len(A) - b_count*(my_len(B)-1)       # (B의 글자수-1)만큼 타이핑 횟수가 적어지는것이므로
    print('#{} {}'.format(t, ans))                # 이에 B의 갯수만큼 곱한걸 빼주고 출력