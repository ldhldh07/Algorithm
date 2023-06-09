import heapq

K, N = map(int, input().split())
prime_numbers = list(map(int, input().split()))

priority_queue = prime_numbers.copy()

for i in range(N-1):
    min_prime_number = heapq.heappop(priority_queue)
    for prime_number in prime_numbers:
        new_prime_number = min_prime_number * prime_number
        if new_prime_number < 2**31 and new_prime_number not in priority_queue:
            heapq.heappush(priority_queue, new_prime_number)
        if min_prime_number % prime_number == 0:
            break    

print(heapq.heappop(priority_queue))