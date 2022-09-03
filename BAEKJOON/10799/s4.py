arr=list(input())
stack = []

ans = 0

for i in range(len(arr)):
    if arr[i] =='(':
        stack.append('(')
        ans += 1
    else:
        if arr[i-1] == '(':
            stack.pop()       
            ans += len(stack)-1
        else:
            stack.pop()
        
print(ans)