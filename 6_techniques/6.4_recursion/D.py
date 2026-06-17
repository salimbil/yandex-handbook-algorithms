# Компилятор: Python 3.11
N, K = map(int, input().split())

def generate(prefix):
    if len(prefix) == N:
        print(''.join(map(str, prefix)))
        return
    
    if not prefix:
        start = 1  # первая цифра не может быть 0
        for d in range(start, 10):
            generate([d])
    else:
        last = prefix[-1]
        # Следующая цифра: last + K или last - K
        if last + K <= 9:
            generate(prefix + [last + K])
        if last - K >= 0 and K != 0:  # при K=0 не дублируем
            generate(prefix + [last - K])

generate([])
