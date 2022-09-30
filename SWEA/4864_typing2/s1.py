# 4861_문자열
# 2022-08-16

def my_len(my_list):                                       # len 역할 하는 함수 선언
    lenlen = 0
    for _ in my_list:
        lenlen += 1
    return lenlen

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    
    for a in range(my_len(str2) - my_len(str1) + 1):       # A를 B의 length만큼 슬라이싱해서 반복
        if str2[a:a + my_len(str1)] == str1 :              # 슬라이싱한 리스트가 B리스트와 같으면
            ans = 1                                        # 1 출력
            break
        else:
            ans = 0                                        # 아닌 경우 0
            
    print('#{} {}'.format(t, ans))