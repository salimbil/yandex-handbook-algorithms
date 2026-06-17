// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <numeric>
#include <cmath>

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    long long a, b, c;
    if (std::cin >> a >> b >> c) {
        // Если оба коэффициента равны 0
        if (a == 0 && b == 0) {
            if (c == 0) {
                std::cout << "YES\n";
            } else {
                std::cout << "NO\n";
            }
        } else {
            // Находим НОД от абсолютных значений, чтобы избежать проблем со знаком
            long long g = std::gcd(std::abs(a), std::abs(b));
            
            // Если c делится на НОД(a, b) без остатка
            if (c % g == 0) {
                std::cout << "YES\n";
            } else {
                std::cout << "NO\n";
            }
        }
    }

    return 0;
}
