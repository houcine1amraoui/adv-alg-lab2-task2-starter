def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Compare adjacent elements
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the first element of unsorted part is the minimum
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr, 0

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half, left_comparisons = merge_sort(arr[:mid])
    right_half, right_comparisons = merge_sort(arr[mid:])

    # Merge step
    merged, merge_comparisons = merge(left_half, right_half)

    # Total comparisons = left + right + merge
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons

    return merged, total_comparisons


def merge(left, right):
    """merge two sorted lists and count comparisons."""
    merged = []
    i = j = 0
    comparisons = 0  # counter for number of element comparisons

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        comparisons += 1  # every comparison of left[i] and right[j]
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, comparisons