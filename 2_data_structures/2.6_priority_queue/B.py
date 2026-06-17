# Компилятор: Python 3.13.2
import heapq

def solve():
    n = int(input())
    tickets = []
    for _ in range(n):
        d, w = map(int, input().split())
        tickets.append((-w, d))  # минус для макс-кучи

    # Куча тикетов: max по w, min по d при равных w
    heapq.heapify(tickets)

    # Куча сотрудников: мин по времени окончания (освобождения)
    workers = [0, 0]  # начальное время освобождения
    heapq.heapify(workers)

    while tickets:
        w_neg, d = heapq.heappop(tickets)
        w = -w_neg

        # Время начала = время освобождения первого свободного сотрудника
        free_time = heapq.heappop(workers)
        finish_time = free_time + d
        heapq.heappush(workers, finish_time)

    # Общее время = максимальное время окончания среди сотрудников
    total_time = max(workers)
    print(total_time)

if __name__ == "__main__":
    solve()
