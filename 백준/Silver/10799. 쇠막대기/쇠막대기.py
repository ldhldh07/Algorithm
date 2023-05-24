arr=list(input())
stack = [0] * (len(arr) // 2)
top = -1

ans = 0
top = 0
stack[top] = arr[0]

for i in range(1,len(arr)):
    if arr[i] =='(':
        top += 1
        ans += 1
        stack[top] = '('
    else:
        if arr[i-1] == '(':
            top -= 1        
            ans += top
        else:
            top -= 1
        
print(ans+1)