# Компилятор: Python 3.13.2
def count_comparisons(arr):
    n = len(arr)
    total_comparisons = 0

    def median_of_three_index(l, r):
        mid = (l + r) // 2
        candidates = [(arr[l], l), (arr[mid], mid), (arr[r], r)]
        candidates.sort(key=lambda x: x[0])
        return candidates[1][1]  # индекс медианного по значению

    def partition(l, r):
        nonlocal total_comparisons
        # выбор медианы трёх и обмен с a[r]
        median_idx = median_of_three_index(l, r)
        arr[median_idx], arr[r] = arr[r], arr[median_idx]

        pivot = arr[r]
        # сравнения происходят в цикле ниже
        comparisons_in_this_call = r - l
        total_comparisons += comparisons_in_this_call

        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def quicksort(l, r):
        if l >= r:
            return
        pos = partition(l, r)
        quicksort(l, pos - 1)
        quicksort(pos + 1, r)

    quicksort(0, n - 1)
    return total_comparisons

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    result = count_comparisons(arr)
    print(result)
