// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    Point() {}
    Point(long long x, long long y) : x(x), y(y) {}
};

struct Segment {
    Point p1, p2;
    Segment() {}
    Segment(long long x1, long long y1, long long x2, long long y2) : p1(x1, y1), p2(x2, y2) {}
};

// Ориентированная площадь * 2 (знак)
long long orient(const Point &a, const Point &b, const Point &c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

// Проверка, лежит ли точка c на отрезке ab
bool onSegment(const Point &a, const Point &b, const Point &c) {
    return min(a.x, b.x) <= c.x && c.x <= max(a.x, b.x) &&
           min(a.y, b.y) <= c.y && c.y <= max(a.y, b.y);
}

// Проверка пересечения двух отрезков
bool segmentsIntersect(const Segment &s1, const Segment &s2) {
    long long o1 = orient(s1.p1, s1.p2, s2.p1);
    long long o2 = orient(s1.p1, s1.p2, s2.p2);
    long long o3 = orient(s2.p1, s2.p2, s1.p1);
    long long o4 = orient(s2.p1, s2.p2, s1.p2);

    // Общий случай: знаки разные
    if (o1 > 0 && o2 > 0) return false;
    if (o1 < 0 && o2 < 0) return false;
    if (o3 > 0 && o4 > 0) return false;
    if (o3 < 0 && o4 < 0) return false;

    // Если все ориентации нулевые — отрезки коллинеарны
    if (o1 == 0 && o2 == 0 && o3 == 0 && o4 == 0) {
        // Проверяем перекрытие проекций
        if (max(s1.p1.x, s1.p2.x) < min(s2.p1.x, s2.p2.x)) return false;
        if (max(s2.p1.x, s2.p2.x) < min(s1.p1.x, s1.p2.x)) return false;
        if (max(s1.p1.y, s1.p2.y) < min(s2.p1.y, s2.p2.y)) return false;
        if (max(s2.p1.y, s2.p2.y) < min(s1.p1.y, s1.p2.y)) return false;
        return true;
    }

    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Segment> segs(n);
    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        segs[i] = Segment(x1, y1, x2, y2);
    }

    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (segmentsIntersect(segs[i], segs[j])) {
                ++count;
            }
        }
    }

    cout << count << '\n';
    return 0;
}
