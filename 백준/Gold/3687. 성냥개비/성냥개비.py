t = int(input())

n_list = [int(input()) for _ in range(t)]

max_n = max(n_list)

max_num = int('1'* (max_n+1))
min_dp = [max_num for _ in range(max_n+1)] 

min_stick_num = {'0':6,'1':2, '2':5,'4':4,'6':6,'7':3,'8':7}
for num, stick in min_stick_num.items():
    min_dp[stick] = int(num)
for num, stick in min_stick_num.items():
    for i in range(stick, max_n+1):
        if num == '0' and min_dp[i-stick] == 0:
            continue
        min_dp[i] = min(min_dp[i], int(str(min_dp[i-stick])+ num))

max_dp = [0 for _ in range(max_n+1)]
max_stick_num = {'9':6, '8':7, '7':3,'5':5,'4':4,'1':2}

for num, stick in max_stick_num.items():
    for i in range(stick, max_n+1):
        max_dp[i] = max(max_dp[i], int(str(max_dp[i-stick])+num))
    max_dp

for n in n_list:
    print(min_dp[n], max_dp[n])