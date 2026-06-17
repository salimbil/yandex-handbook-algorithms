# Компилятор: Python 3.13.2
import random

def partition(arr, left, right):
    pivot_idx = random.randint(left, right)
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    
    store_idx = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
    
    arr[store_idx], arr[right] = arr[right], arr[store_idx]
    return store_idx

def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_idx = partition(arr, left, right)
    
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quickselect(arr, left, pivot_idx - 1, k)
    else:
        return quickselect(arr, pivot_idx + 1, right, k)

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = quickselect(a, 0, n - 1, k - 1)
print(result)
