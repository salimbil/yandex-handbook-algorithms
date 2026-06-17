# Компилятор: Python 3.13.2
def solve():
    s = input().strip()
    pos = 0
    n = len(s)
    
    def parse_expr():
        nonlocal pos
        val = parse_term()
        while pos < n and s[pos] in ('+', '-'):
            op = s[pos]
            pos += 1
            right = parse_term()
            if op == '+':
                val += right
            else:
                val -= right
        return val
    
    def parse_term():
        nonlocal pos
        val = parse_factor()
        while pos < n and s[pos] == '*':
            pos += 1
            val *= parse_factor()
        return val
    
    def parse_factor():
        nonlocal pos
        if s[pos] == '(':
            pos += 1
            val = parse_expr()
            pos += 1  # skip ')'
            return val
        else:
            # число
            start = pos
            while pos < n and s[pos].isdigit():
                pos += 1
            return int(s[start:pos])
    
    result = parse_expr()
    print(result)

if __name__ == "__main__":
    solve()
