import sys
from collections import deque

si = sys.stdin.readline

# Read inputs
n, w, L = map(int, si().strip().split())  # n: number of trucks, w: bridge length, L: max load
trucks = list(map(int, si().strip().split()))  # List of trucks' weights

# Initialize variables
bridge = deque([0] * w)  # Simulates the bridge with fixed length, starts with no trucks
current_weight = 0  # Current total weight on the bridge
time = 0  # Time counter

for truck in trucks:
    while True:
        # Move time by 1 unit and remove the truck from the front of the bridge
        time += 1
        current_weight -= bridge.popleft()  # Remove the front truck (or zero if none)

        # If adding the next truck doesn't exceed the weight limit
        if current_weight + truck <= L:
            # Add the current truck to the bridge
            bridge.append(truck)
            current_weight += truck
            break
        else:
            # If it exceeds, add a 'zero' (no truck) to simulate a time unit passing without a truck
            bridge.append(0)

# After all trucks are on the bridge, they still need time to fully cross
time += w  # Add the time for the last truck to cross the bridge

print(time)
