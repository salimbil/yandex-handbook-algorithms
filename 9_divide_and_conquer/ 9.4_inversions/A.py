# Компилятор: Python 3.13.2
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    inversions = inv_left + inv_right
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    _, inv_count = merge_sort(arr)
    print(inv_count)

if __name__ == "__main__":
    solve()
