# Компилятор: Python 3.11
a, b, K = map(int, input().split())

# Вычисляем a^b по модулю 10^K
mod = 10 ** K
result = pow(a, b, mod)

# Форматируем с ведущими нулями до K цифр
print(f"{result:0{K}d}")
