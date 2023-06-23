N = int(input())
print(int(''.join(sorted(list(map(str, input().split())), key=lambda x: -int(x * (10 // len(x)) + x[:10 % len(x)])))))