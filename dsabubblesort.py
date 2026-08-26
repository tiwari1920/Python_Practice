print("Bubble Sort Algorithm in Python")
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
def bubbleSort(arr, n):
    for i in range(n):
        isSorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False
        if isSorted:
            break
bubbleSort(arr, n)
print("Sorted array is:", arr)