# Компилятор: Python 3.13.2
def main():
    import sys

    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    coins = []
    
    idx = 1
    for i in range(n):
        c = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        coins.append((c, b))
    
    S = int(input_data[idx])
    
    # Сортируем по убыванию номинала
    coins.sort(key=lambda x: x[0], reverse=True)
    
    total_coins = 0
    remaining = S
    
    for c, b in coins:
        if remaining <= 0:
            break
        
        if b == -1:
            # Бесконечное количество
            count = remaining // c
        else:
            # Ограниченное количество
            count = min(remaining // c, b)
        
        if count > 0:
            remaining -= count * c
            total_coins += count
    
    if remaining > 0:
        print(-1)
    else:
        print(total_coins)

if __name__ == "__main__":
    main()
