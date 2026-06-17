# Компилятор: Python 3.11
K, S = map(int, input().split())

def get_min_palindrome(K, S):
    result = ['0'] * K
    remaining = S
    
    for i in range((K + 1) // 2):
        start = 1 if i == 0 else 0
        for d in range(start, 10):
            if i == K - 1 - i:  # центральная цифра при нечётном K
                if d == remaining:
                    result[i] = str(d)
                    return ''.join(result)
            else:
                if remaining >= 2 * d:
                    # проверяем, можно ли разместить оставшуюся сумму
                    max_possible = 9 * ((K - 1 - i) - i - 1)
                    if remaining - 2 * d <= max_possible:
                        result[i] = result[K - 1 - i] = str(d)
                        remaining -= 2 * d
                        break
    
    return ''.join(result)

def get_max_palindrome(K, S):
    result = ['0'] * K
    remaining = S
    
    for i in range((K + 1) // 2):
        start = 1 if i == 0 else 0
        for d in range(9, start - 1, -1):
            if i == K - 1 - i:  # центральная
                if d == remaining:
                    result[i] = str(d)
                    return ''.join(result)
            else:
                if remaining >= 2 * d:
                    max_possible = 9 * ((K - 1 - i) - i - 1)
                    if remaining - 2 * d <= max_possible:
                        result[i] = result[K - 1 - i] = str(d)
                        remaining -= 2 * d
                        break
    
    return ''.join(result)

print(get_min_palindrome(K, S), get_max_palindrome(K, S))
