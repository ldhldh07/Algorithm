T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())

    charge_list = list(map(int, input().split()))
    charge_list.append(N)                                                  # 마지막 정류장도 충전장소로 더미
    charge_list.insert(0, 0)                                               # 첫 정류장도 더미

    charge_cnt = 0                                                         # 충전 횟수
    prev_charge = 0                                                        # 이전에 충전한 충전소
    run_bus = True                                                         # 버스 운행 여부

    for charge_idx in range(1, M+1):                                       # 충전소별로 반복문
        if charge_list[charge_idx+1] - charge_list[charge_idx] > K:        # 다음 충전소와의 정류장수가 K를 초과하면
            run_bus = False                                                # 운행불가
            break
        elif charge_list[charge_idx+1] - charge_list[prev_charge] > K:     # 다음 충전소와 이전 충전한 충전소간 정류장수가 K를 초과할 때
            charge_cnt += 1                                                # 현 충전소에서 충전하고 충전횟수 누적
            prev_charge = charge_idx                                       # 이전 충전소 업데이트

    if run_bus == False:                                                   # 버스 운행 불가일 때
        print('#{} 0'.format(t))                                           # 0 출력
    else:                                                                  # 그렇지 않을 때
        print('#{} {}'.format(t, charge_cnt))                              # 누적된 충전횟수 출력