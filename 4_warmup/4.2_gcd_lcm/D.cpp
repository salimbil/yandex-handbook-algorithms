// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <numeric> // Для std::gcd

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    long long a, b, c, d;
    if (std::cin >> a >> b >> c >> d) {
        // Вычисляем новый числитель и знаменатель.
        // Переменные могут достигать 2 * 10^18, поэтому обязательно используем long long.
        long long num = a * d + c * b;
        long long den = b * d;

        // Находим НОД числителя и знаменателя для сокращения
        long long g = std::gcd(num, den);

        // Выводим сокращенную дробь
        std::cout << num / g << " " << den / g << "\n";
    }

    return 0;
}
