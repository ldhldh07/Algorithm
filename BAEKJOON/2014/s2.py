import heapq

K, N = map(int, input().split())
prime_numbers = list(map(int, input().split()))

priority_queue = []
for prime_number in prime_numbers:
    heapq.heappush(priority_queue, (prime_number, prime_number)) 

for _ in range(N):
    print(priority_queue)
    min_prime_number, first_prime_number = heapq.heappop(priority_queue)
    for prime_number in prime_numbers:
        if prime_number > first_prime_number: 
            break
        new_prime_number = min_prime_number * prime_number
        heapq.heappush(priority_queue, (new_prime_number, prime_number))

print(min_prime_number)