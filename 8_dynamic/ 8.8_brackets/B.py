# Компилятор: Python 3.13.2
def solve():
    s = input().strip()
    
    # Парсим токены
    tokens = []
    i = 0
    n = len(s)
    while i < n:
        if s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            tokens.append(int(s[i:j]))
            i = j
        else:
            tokens.append(s[i])
            i += 1
    
    # Сначала вычисляем умножения
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            left = tokens[i-1]
            right = tokens[i+1]
            val = left * right
            tokens[i-1:i+2] = [val]
            # i остаётся на том же месте (теперь это число)
        else:
            i += 1
    
    # Теперь только + и -
    result = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = tokens[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        i += 2
    
    print(result)

if __name__ == "__main__":
    solve()
