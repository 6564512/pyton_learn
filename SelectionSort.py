def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    arr = [2, 44, 5, 6, 7, 56]
    print(arr)
    SelectionSort(arr)
    print(arr)
