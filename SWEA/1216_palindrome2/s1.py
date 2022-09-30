T = 10

for _ in range(T):
    t = int(input())
    arr = [input() for _ in range(100)]

    for length in range(1,101):               # 회문의 글자수 반복
        word_list = []
        for i in range(100):
            for j in range(100-length+1):     # 가로에 그 글자수 단어 word_list에 추가
                row_word=arr[i][j:j+length]
                word_list.append(row_word)

        for j in range(100):                  # 세로에 그 글자수 단어 word_list에 추가
            for i in range(100-length+1):
                col_word = ''
                for l in range(length):
                    col_word += arr[i+l][j]
                word_list.append(col_word)
  
        for word in word_list:                # 리스트 중에 회문 있으면 ans 갱신
            if word == word[::-1]:            # 반복문이므로 가장 큰 값이 ans에 들어감
                ans = length

    print('#{} {}'.format(t, ans))            # ans 출력