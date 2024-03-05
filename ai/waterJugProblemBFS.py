from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target_amount):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        current_state = queue.popleft()
        jug1_amount, jug2_amount = current_state
        print(f"Current state: ({jug1_amount} liters, {jug2_amount} liters)")
        if jug1_amount == target_amount or jug2_amount == target_amount:
            print("Target amount reached!")
            return current_state
        if current_state in visited:
            print("Already visited, skipping...")
            continue
        visited.add(current_state)
        print("Fill jug1")
        queue.append((jug1_capacity, jug2_amount))
        print("Fill jug2")
        queue.append((jug1_amount, jug2_capacity))
        print("Empty jug1")
        queue.append((0, jug2_amount))
        print("Empty jug2")
        queue.append((jug1_amount, 0))
        pour_amount = min(jug1_amount, jug2_capacity - jug2_amount)
        print(f"Pour from jug1 to jug2: {pour_amount} liters")
        queue.append((jug1_amount - pour_amount, jug2_amount + pour_amount))
        pour_amount = min(jug2_amount, jug1_capacity - jug1_amount)
        print(f"Pour from jug2 to jug1: {pour_amount} liters")
        queue.append((jug1_amount + pour_amount, jug2_amount - pour_amount))
    return None


jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target_amount = int(input("Enter the target amount of water: "))
result = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
if result:
    print(f"Target amount {target_amount} liters can be measured with ({result[0]} liters, {result[1]} liters) in the jugs.")
else:
    print("Target amount cannot be measured with the given jug capacities.")
