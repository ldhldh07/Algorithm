K, N = map(int, input().split())

prime_numbers = list(map(int, input().split()))

def get_ans(prime_number_list, n):
    index = 0
    for a in range(1, 2**31):
        current_a = a
        while True:
            for prime_number in prime_number_list:
                if not current_a % prime_number:
                    current_a //= prime_number
                    break
            else:
                break
            if current_a == 1:
                index += 1
                break
        if index == n:
            return a
            
            
print(get_ans(prime_numbers, N))