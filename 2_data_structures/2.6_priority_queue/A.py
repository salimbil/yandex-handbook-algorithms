# Компилятор: Python 3.13.2
import sys
import heapq

def main():
    input = sys.stdin.read().split()
    q = int(input[0])
    
    heap = []
    idx = 1
    
    results = []
    
    for _ in range(q):
        query_type = int(input[idx])
        idx += 1
        
        if query_type == 1:
            x = int(input[idx])
            idx += 1
            heapq.heappush(heap, -x)
        else:
            # Проверяем, не пуста ли очередь перед удалением
            if heap:
                heapq.heappop(heap)
        
        # Выводим текущий максимальный элемент
        if heap:
            results.append(str(-heap[0]))
        else:
            results.append("-1")
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
