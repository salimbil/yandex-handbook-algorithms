// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

struct Point {
    long long x, y;
    int idx;
};

bool cmpX(const Point& a, const Point& b) {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

bool cmpY(const Point& a, const Point& b) {
    return a.y < b.y;
}

double dist(const Point& a, const Point& b) {
    long long dx = a.x - b.x;
    long long dy = a.y - b.y;
    return sqrt(dx*dx + dy*dy);
}

pair<double, pair<int, int>> bruteForce(const vector<Point>& points, int left, int right) {
    double minDist = 1e20;
    int idx1 = 0, idx2 = 1;
    
    for (int i = left; i < right; ++i) {
        for (int j = i + 1; j < right; ++j) {
            double d = dist(points[i], points[j]);
            if (d < minDist) {
                minDist = d;
                idx1 = points[i].idx;
                idx2 = points[j].idx;
            }
        }
    }
    return {minDist, {min(idx1, idx2), max(idx1, idx2)}};
}

pair<double, pair<int, int>> closestUtil(vector<Point>& points, int left, int right) {
    if (right - left <= 3) {
        return bruteForce(points, left, right);
    }
    
    int mid = (left + right) / 2;
    Point midPoint = points[mid];
    
    auto leftRes = closestUtil(points, left, mid);
    auto rightRes = closestUtil(points, mid, right);
    
    auto best = (leftRes.first < rightRes.first) ? leftRes : rightRes;
    double d = best.first;
    
    vector<Point> strip;
    for (int i = left; i < right; i++) {
        if (abs(points[i].x - midPoint.x) < d) {
            strip.push_back(points[i]);
        }
    }
    
    sort(strip.begin(), strip.end(), cmpY);
    
    for (size_t i = 0; i < strip.size(); ++i) {
        for (size_t j = i + 1; j < strip.size() && (strip[j].y - strip[i].y) < d; ++j) {
            double currDist = dist(strip[i], strip[j]);
            if (currDist < d) {
                d = currDist;
                int idx1 = strip[i].idx;
                int idx2 = strip[j].idx;
                best = {d, {min(idx1, idx2), max(idx1, idx2)}};
            }
        }
    }
    
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<Point> points(n);
    for (int i = 0; i < n; ++i) {
        cin >> points[i].x >> points[i].y;
        points[i].idx = i + 1;
    }
    
    sort(points.begin(), points.end(), cmpX);
    
    auto result = closestUtil(points, 0, n);
    
    cout << fixed << setprecision(10) << result.first << "\n";
    cout << result.second.first << " " << result.second.second << "\n";
    
    return 0;
}
