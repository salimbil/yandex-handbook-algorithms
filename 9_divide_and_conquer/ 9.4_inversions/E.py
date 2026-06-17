# Компилятор: Python 3.13.2
def count_inversions(arr):
    def merge_sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_l = merge_sort(a[:mid])
        right, inv_r = merge_sort(a[mid:])
        merged = []
        i = j = 0
        inv = inv_l + inv_r
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv
    _, inv = merge_sort(arr)
    return inv

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    posB = [0] * (n + 1)
    for i, val in enumerate(B):
        posB[val] = i
    
    # Массив позиций элементов A в B
    posAinB = [posB[x] for x in A]
    
    inv_count = count_inversions(posAinB)
    print(inv_count)

if __name__ == "__main__":
    solve()
