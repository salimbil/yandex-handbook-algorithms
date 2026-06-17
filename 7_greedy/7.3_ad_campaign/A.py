# Компилятор: Python 3.13.2
def main():
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    
    # Сортируем оба массива по убыванию
    prices.sort(reverse=True)
    clicks.sort(reverse=True)
    
    # Считаем максимальную прибыль
    profit = sum(prices[i] * clicks[i] for i in range(n))
    
    print(profit)

if __name__ == "__main__":
    main()
