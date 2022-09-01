N = int(input())
a = N % 15  # 나머지
if a in [1,2,4,7]: # 나머지가 3,5의 합으로 불가능 한 숫자면
    ans = -1
else:
    if a % 5 == 0: # 나머지가 5의 배수면 그냥 5로 나눈 몫
        ans = N // 5
    elif a % 3 == 0: # 나머지가 3의 배수면
        ans = 3 * (N // 15) + (a//3)
    elif a in [8, 13]: # 나머지가 8 혹은 13 이면
        ans = (N // 5)  + 1
    elif a in [11, 14]:
        ans = 3 * (N // 15) + ((a -5)// 3)+1

print(ans)
