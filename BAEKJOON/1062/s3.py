from collections import defaultdict

alphabets = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm','o','p','q','r','s','u','v','w','x','y','z']

N, K = map(int, input().split())


for index in range(N):
    char_dict = defaultdict(int)
    word = input()
    print(word[4:-4])
    for char in word[4:-4]:
        char_dict[char] = 1
        
    for key, value in char_dict.items():
        print(key, value)
        