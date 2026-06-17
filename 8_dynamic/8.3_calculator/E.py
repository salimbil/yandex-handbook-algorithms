# Компилятор: Python 3.13.2
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1

    queries = []
    for _ in range(M):
        queries.append(int(data[idx])); idx += 1

    INF = 10**9
    dist = [INF] * (N + 1)
    prev = [-1] * (N + 1)

    dist[1] = 0

    for x in range(1, N + 1):
        # +1, +2, +3
        for d in range(1, 4):
            if x + d <= N and dist[x + d] > dist[x] + 1:
                dist[x + d] = dist[x] + 1
                prev[x + d] = x
        # *2, *3
        for m in (2, 3):
            if x * m <= N and dist[x * m] > dist[x] + 1:
                dist[x * m] = dist[x] + 1
                prev[x * m] = x

    out_lines = []
    for t in queries:
        path = []
        cur = t
        while cur != -1:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        out_lines.append(" ".join(map(str, path)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
