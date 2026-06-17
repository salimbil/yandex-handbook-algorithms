// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <numeric> // Для std::gcd

int main() {
    // Оптимизация ввода-вывода для ускорения работы программы
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    // Используем long long, так как числа достигают 2 * 10^9
    long long a, b;
    if (std::cin >> a >> b) {
        std::cout << std::gcd(a, b) << "\n";
    }

    return 0;
}
