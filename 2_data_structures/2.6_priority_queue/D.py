# Компилятор: Python 3.13.2
import heapq

def solve():
    n, k = map(int, input().split())
    heap = []  # куча с временами отъезда
    count = 0

    for _ in range(n):
        a, b = map(int, input().split())
        # Удаляем машины, которые уехали до времени a
        while heap and heap[0] <= a:
            heapq.heappop(heap)
        # Если есть свободное место
        if len(heap) < k:
            heapq.heappush(heap, b)
            count += 1
    print(count)

if __name__ == "__main__":
    solve()
