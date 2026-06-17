# Компилятор: Python 3.11
import sys
from collections import deque

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n, m = map(int, data[0].split())
    grid = data[1:1+n]
    
    sx = sy = fx = fy = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx, sy = i, j
            elif grid[i][j] == 'F':
                fx, fy = i, j
    
    INF = 10**9
    dist = [[INF] * m for _ in range(n)]
    dist[sx][sy] = -1
    
    dq = deque()
    dq.append((sx, sy))
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while dq:
        x, y = dq.popleft()
        cur = dist[x][y]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            step = 0
            while 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                if dist[nx][ny] > cur + 1:
                    dist[nx][ny] = cur + 1
                    dq.append((nx, ny))
                nx += dx
                ny += dy
                step += 1
    
    ans = dist[fx][fy]
    print(-1 if ans == INF else ans)

if __name__ == '__main__':
    solve()
