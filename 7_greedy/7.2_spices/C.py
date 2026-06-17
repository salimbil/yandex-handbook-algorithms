# Компилятор: Python 3.13.2
import sys
from bisect import bisect_right

def main():
    data = sys.stdin.read().split()
    
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    
    items = []
    for _ in range(n):
        price = int(next(it))
        discount = int(next(it))
        # Вычисляем итоговую стоимость (вес) для задачи о рюкзаке
        cost = price - discount 
        items.append((cost, discount))
    
    S = int(next(it))

    # Список недоминируемых состояний: (total_cost, total_discount)
    # Список всегда отсортирован по total_cost.
    # Для одинаковой стоимости мы храним только состояние с максимальной скидкой.
    states = [(0, 0)]

    for cost, discount in items:
        # Если стоимость товара 0 (полностью бесплатный после скидки),
        # мы просто добавляем его скидку ко всем существующим состояниям.
        if cost == 0:
            states = [(c, d + discount) for c, d in states]
            continue

        # Генерируем новые состояния, добавляя текущий товар к существующим
        new_states = []
        for total_cost, total_discount in states:
            new_cost = total_cost + cost
            if new_cost <= S:
                new_states.append((new_cost, total_discount + discount))
        
        # Объединяем старые и новые состояния
        merged = states + new_states
        
        # Сортируем по стоимости, а при равной стоимости - по скидке по убыванию
        merged.sort()

        # Очищаем список от доминируемых состояний
        new_clean_states = []
        max_discount_so_far = -1
        
        for total_cost, total_discount in merged:
            # Состояние полезно, только если его скидка больше любого предыдущего
            # с меньшей или равной стоимостью.
            if total_discount > max_discount_so_far:
                new_clean_states.append((total_cost, total_discount))
                max_discount_so_far = total_discount
        
        states = new_clean_states

    # Находим максимальную скидку среди всех оставшихся состояний
    # (все они уже удовлетворяют условию по бюджету)
    max_discount = max(d for _, d in states)
    
    print(max_discount)

if __name__ == "__main__":
    main()
