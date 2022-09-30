# 1952_수영장 풀이
# 2022-09-23

def less(a, b):                                                 # 두 개의 금액 중 더 작은 것을 반환하는 함수입니다
    return a if a < b else b


T = int(input())

for t in range(1, 1+T):
    day, month, three_month, year = map(int, input().split())
    plans = [n * day for n in list(map(int, input().split()))]  # 일요금 X 월별 이용일을 받아서 리스트를 만듭니다

    for i, plan in enumerate(plans):                            # 월별로 월요금과 총 지불 비교합니다
        plans[i] = less(plan, month)                            # 더 적은 것으로 최신화합니다

    new_plan = [0] * 12                                         # 3달치 최소금액은 그 3달전까지 낸 최소금액에 3달 요금 내거나
    new_plan[0], new_plan[1] = plans[0], plans[0] + plans[1]    # 1달전까지 낸 최소금액에 1달 요금 낸 것 중 더 작은 값입니다
    new_plan[2] = less(plans[0] + plans[1] + plans[2], three_month)  # 3월까지 최소금액은 계산해서 넣어줍니다

    for i in range(3, 12):                                      # 4월부터 위 기준으로 더 작은 값 새로운 리스트에 넣어줍니다
        new_plan[i] = less(new_plan[i-3] + three_month, new_plan[i-1] + plans[i])

    print('#{} {}'.format(t, less(new_plan[11], year)))            # 연요금과 비교해서 더 적은 것 출력합니다