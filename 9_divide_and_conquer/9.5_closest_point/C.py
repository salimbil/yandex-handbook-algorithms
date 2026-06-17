# Компилятор: Python 3.13.2
import sys
import math

def solve():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[3*i + 1])
        y = int(data[3*i + 2])
        z = int(data[3*i + 3])
        points.append((x, y, z))
    
    points.sort(key=lambda p: p[0])
    best_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, min(n, i + 30)):  # смотрим только следующие 30 точек
            dx = points[i][0] - points[j][0]
            if dx * dx >= best_dist:
                break
            dy = points[i][1] - points[j][1]
            dz = points[i][2] - points[j][2]
            dist2 = dx*dx + dy*dy + dz*dz
            if dist2 < best_dist:
                best_dist = dist2
    print(math.sqrt(best_dist))

if __name__ == "__main__":
    solve()
