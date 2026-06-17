# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    vals = list(map(int, input().split()))
    total = sum(vals)
    
    if total % 3 != 0:
        print(0)
        return
    
    target = total // 3
    vals.sort(reverse=True)  # эвристика для ускорения
    
    memo = {}
    
    def dfs(i, a, b, c):
        if i == n:
            return a == target and b == target and c == target
        
        key = (i, a, b, c)
        if key in memo:
            return memo[key]
        
        w = vals[i]
        
        # пробуем положить в первую
        if a + w <= target and dfs(i + 1, a + w, b, c):
            memo[key] = True
            return True
        # во вторую
        if b + w <= target and dfs(i + 1, a, b + w, c):
            memo[key] = True
            return True
        # в третью
        if c + w <= target and dfs(i + 1, a, b, c + w):
            memo[key] = True
            return True
        
        memo[key] = False
        return False
    
    result = dfs(0, 0, 0, 0)
    print(1 if result else 0)

if __name__ == "__main__":
    solve()
