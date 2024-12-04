from DataClean import get_data

def merge(left, right):
    # Merge two sorted lists into single sorted list
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:  # Compare based on covid_cases_per_100k
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from both lists
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def mergesort_recursive(data):
    # recursively sort list of tuples using Merge Sort algorithm
    if len(data) <= 1:
        return data

    # Split the data into two halves
    mid = len(data) // 2
    left = mergesort_recursive(data[:mid])
    right = mergesort_recursive(data[mid:])

    # Merge the sorted halves
    return merge(left, right)

def mergesort() -> list[tuple]:
    # Sort the data from get_data using Merge Sort algorithm
    data = get_data()
    return mergesort_recursive(data)

