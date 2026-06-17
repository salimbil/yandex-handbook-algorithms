# Компилятор: Python 3.13.2
import sys

def main():
    data = sys.stdin.read().split()
    
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    W = float(next(it)) # Вместимость может быть большой, используем float для точности
    k = float(next(it))
    
    items = []
    for _ in range(n):
        w = int(next(it))
        c = int(next(it))
        density = c / w
        items.append((density, w, c))
    
    # Сортируем по убыванию удельной ценности (плотности)
    items.sort(key=lambda x: x[0], reverse=True)
    
    total_cost = 0.0
    remaining_capacity = W

    for density, w, c in items:
        if remaining_capacity <= 0:
            break
            
        # Вычисляем максимальную долю товара, которую можем взять,
        # чтобы либо заполнить рюкзак, либо взять весь товар целиком.
        # effective_weight_per_unit - это фактическая масса единицы исходной массы товара.
        effective_weight_per_unit = w * (1 - k)
        
        # Доля x, которая полностью исчерпает оставшуюся вместимость.
        x_to_fill_capacity = remaining_capacity / effective_weight_per_unit
        
        # Мы не можем взять больше целого товара.
        x = min(1.0, x_to_fill_capacity)
        
        total_cost += x * c
        
        # Обновляем оставшуюся вместимость
        remaining_capacity -= x * effective_weight_per_unit

    # Выводим результат с точностью до 6 знаков после запятой
    print(f"{total_cost:.6f}")

if __name__ == "__main__":
    main()
