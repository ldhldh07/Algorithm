G, P = int(input()), int(input())

gates = [0 for _ in range(G+1)]
cnt = 0
flag = True

for i in range(1, P+1):
    g = int(input())
    if flag:
        for gate in range(g, 0, -1):
            if not gates[g]:
                gates[g] = i
                cnt += 1
                break
            g = g-1
        else:
            flag = False
    
print(cnt)

