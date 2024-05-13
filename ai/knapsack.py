def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    total_value = dp[n][capacity]
    remaining_capacity = capacity
    for i in range(n, 0, -1):
        if total_value <= 0:
            break
        if total_value != dp[i - 1][remaining_capacity]:
            selected_items.append(i - 1)
            total_value -= values[i - 1]
            remaining_capacity -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
