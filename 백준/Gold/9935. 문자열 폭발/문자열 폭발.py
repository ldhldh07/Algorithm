word = input()
bomb = input()
bomb_length = len(bomb)

stack = []
top = -1

for char in word:
    stack.append(char)
    top += 1
    if top >= bomb_length - 1:
        # 한번 터지면 계속 체크해야함
        contain_bomb = True
        while contain_bomb and top > -1:
            for i in range(bomb_length):
                if stack[top-i] != bomb[bomb_length-1-i]:
                    contain_bomb = False
                    break 
            else:
                del stack[-bomb_length:]
                top -= bomb_length

print(''.join(stack)) if stack else print('FRULA')