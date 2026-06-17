# Компилятор: Python 3.11
import sys
import heapq

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    q = int(next(it))
    
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        g[u].append((v, w))
        g[v].append((u, w))
    
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    
    for s in range(n):
        d = dist[s]
        d[s] = 0
        pq = [(0, s)]
        while pq:
            cur_d, u = heapq.heappop(pq)
            if cur_d != d[u]:
                continue
            for v, w in g[u]:
                if d[v] > cur_d + w:
                    d[v] = cur_d + w
                    heapq.heappush(pq, (d[v], v))
    
    out = []
    for _ in range(q):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        ans = dist[x][y]
        out.append(str(-1 if ans == INF else ans))
    
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
