T = 10

for t in range(1,1+T):
    N = int(input())
    password = input().split()
    M = int(input())
    com_input = input().split()
    for i, c in enumerate(com_input):
        if c == 'I':
            for a in range(int(com_input[i+2])):
                password.insert(int(com_input[i+1]), com_input[i+2+int(com_input[i+2])-a])
        elif c == 'D':
            for _ in range(int(com_input[i+2])):
                password.pop(int(com_input[i+1]))
        elif c == 'A':
            for b in range(int(com_input[i+1])):
                password.append(com_input[i+1+int(com_input[i+1])-b])
    ans_list = []
    for idx in range(10):
        ans_list.append(password[idx])

    print('#{}'.format(t), ' '.join(ans_list))