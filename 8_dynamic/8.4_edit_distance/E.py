# Компилятор: Python 3.13.2
from collections import deque

def solve():
    s = input().strip()
    k = int(input())
    n = len(s)
    
    visited = set()
    queue = deque()
    
    start = s
    visited.add(start)
    queue.append((start, 0))
    
    count = 1
    
    while queue:
        cur, dist = queue.popleft()
        
        if dist >= k:
            continue
        
        for i in range(len(cur)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != cur[i]:
                    nxt = cur[:i] + c + cur[i+1:]
                    if nxt not in visited and len(nxt) <= n:
                        visited.add(nxt)
                        queue.append((nxt, dist + 1))
                        count += 1
        
        for i in range(len(cur) + 1):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nxt = cur[:i] + c + cur[i:]
                if nxt not in visited and len(nxt) <= n:
                    visited.add(nxt)
                    queue.append((nxt, dist + 1))
                    count += 1
        
        for i in range(len(cur)):
            nxt = cur[:i] + cur[i+1:]
            if nxt not in visited and len(nxt) <= n:
                visited.add(nxt)
                queue.append((nxt, dist + 1))
                count += 1
    
    print(count)

if __name__ == "__main__":
    solve()
