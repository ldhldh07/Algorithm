arr=list(input())
stack = [0] * 5000
top = -1

ans = 0

for a in arr:
    if a =='(':
        top += 1
        ans += 1
        stack[top] = a
    else:
        if last_a == '(':
            ans += top - 1
            top -= 1        
        else:
            top -= 1
    last_a = a
        
print(ans)