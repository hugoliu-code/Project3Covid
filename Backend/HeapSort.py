from DataClean import get_data

def heapsort() -> list[tuple]:
    # implement a heapsort using the data from get_data
    data = get_data()
    buildMaxHeap(data)
    
    for i in range(len(data) - 1, 0, -1):
        temp = data[0]
        data[0] = data[i]
        data[i] = temp
        heapifyDown(data, 0, i)
    
    return data

def buildMaxHeap(data):
    for i in range(len(data)//2, -1, -1):
        heapifyDown(data, i, len(data))

def heapifyDown(data, i, size):
    left = i * 2 + 1
    right = left + 1
    max = i

    if left < size and data[left][2] > data[max][2]:
        max = left
    if right < size and data[right][2] > data[max][2]:
        max = right

    if max != i:
        temp = data[i]
        data[i] = data[max]
        data[max] = temp
        heapifyDown(data, max, size)