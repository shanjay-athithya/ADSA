from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def merge_sort_parallel(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    count = multiprocessing.cpu_count()
    with ProcessPoolExecutor(max_workers= count) as executor:
        left_sorted, right_sorted = executor.map(merge_sort_parallel, [left, right])

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort_parallel(arr)
    print(f"Sorted array: {sorted_arr}")
