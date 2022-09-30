
T = 10

for t in range(1, T+1):
    dump = int(input())
    tower = list(map(int, input().split()))


    def max_min(num_list):                              #최대 최소값 구하는 함수 선언
        max_num = num_list[0]
        min_num = num_list[0]
        for a in num_list:
            if a > max_num:
                max_num = a
        for b in num_list:
            if b < min_num:
                min_num = b
        return max_num, min_num
    
    max_idx = 0
    min_idx = 0
    diff = max_min(tower)[0]-max_min(tower)[1]

    for _ in range(dump):                              # 덤프 수만큼 반복문
        
        if  max_min(tower)[0]-max_min(tower)[1] <= 1 : # 최대 최소 차이가 1이하면 그 값이 최종값
            diff = max_min(tower)[0]-max_min(tower)[1] 
        else :                                         
            for i in range(100) :                      # 최대값, 최소값을 가진 탑 찾음
                if tower[i] == max_min(tower)[0]:
                    max_idx = i
            for ii in range(100) :    
                if tower[ii] == max_min(tower)[1]:
                    min_idx = ii
        
            tower[max_idx] -= 1                         # 최대값은 -1 최솟값은 +1 해줌
            tower[min_idx] += 1
            diff = max_min(tower)[0]-max_min(tower)[1]  # 이후 최대 최솟값을 diff 변수에 넣음 

        
        
    print('#{} {}'.format(t,diff))
        
