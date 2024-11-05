def knapsack(weights, values, cap):
    n = len(weights)
    
    def knapsack_recursive(index, current_weight, current_value, max_value):
        if index == n:
            return max(max_value, current_value)
            
        if current_weight > cap:
            return max_value
            
        max_value = knapsack_recursive(index + 1, current_weight + weights[index], current_value + values[index], max_value)
        max_value = knapsack_recursive(index + 1, current_weight, current_value, max_value)
        
        return max_value
    
    return knapsack_recursive(0, 0, 0, 0)

if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("Maximum value:", knapsack(weights, values, capacity))
