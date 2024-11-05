def knapsack_approximation(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for _, i in ratio:
        if total_weight + weights[i] <= capacity:
            total_value += values[i]
            total_weight += weights[i]
            selected_items.append(i)

    return total_value, selected_items

# Example usage
if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    max_value, selected_items = knapsack_approximation(weights, values, capacity)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)
