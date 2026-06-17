// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <numeric> // Для std::gcd

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    // Используем unsigned long long, так как НОК может достигать 4 * 10^18
    unsigned long long a, b;
    if (std::cin >> a >> b) {
        // Сначала делим, потом умножаем, чтобы избежать переполнения
        unsigned long long lcm = (a / std::gcd(a, b)) * b;
        std::cout << lcm << "\n";
    }

    return 0;
}
