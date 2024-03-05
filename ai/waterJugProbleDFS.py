def dfs_jug_problem(jug1_capacity, jug2_capacity, target):
    stack = [(0, 0)]  # Initial state of jugs (0, 0)
    visited = set()   # Set to keep track of visited states

    while stack:
        current_state = stack.pop()
        jug1, jug2 = current_state
        print("jug 1: ",jug1,"jug 2: ",jug2)
        if current_state in visited:
            continue

        visited.add(current_state)

        # Check if target state is reached
        if jug1 == target or jug2 == target:
            return True

        # Fill jug1
        if jug1 < jug1_capacity:
            stack.append((jug1_capacity, jug2))

        # Fill jug2
        if jug2 < jug2_capacity:
            stack.append((jug1, jug2_capacity))

        # Empty jug1
        if jug1 > 0:
            stack.append((0, jug2))

        # Empty jug2
        if jug2 > 0:
            stack.append((jug1, 0))

        # Pour water from jug1 to jug2
        if jug1 > 0 and jug2 < jug2_capacity:
            amount = min(jug1, jug2_capacity - jug2)
            print("amount: ",amount)
            stack.append((jug1 - amount, jug2 + amount))

        # Pour water from jug2 to jug1
        if jug2 > 0 and jug1 < jug1_capacity:
            amount = min(jug2, jug1_capacity - jug1)
            print("amount: ",amount)
            stack.append((jug1 + amount, jug2 - amount))

    return False

# Take user input for jug capacities and target amount
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter the target amount: "))

# Check if the target amount is reachable
if dfs_jug_problem(jug1_capacity, jug2_capacity, target):
    print(f"The target amount of {target} liters is reachable.")
else:
    print(f"The target amount of {target} liters is not reachable.")
