

arr=list(input())
stack = [0] * 20
top = -1

ans = 0

for a in arr:
    if a =='(':
        top += 1
        stack[top] = a
    elif a == ')':
        top -= 1
        if stack[top+1] == '(':
            ans += top + 1
print(ans)


