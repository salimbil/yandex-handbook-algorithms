// Компилятор: C++23 (GCC 14.1)
#include <iostream>

int main() {
    // Ускорение ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    long long n;
    if (std::cin >> n) {
        // Начальные числа Фибоначчи
        long long a = 1;
        long long b = 1;

        // Генерируем числа Фибоначчи, пока следующее (их сумма) не превысит n
        while (a + b <= n) {
            long long next = a + b;
            a = b;
            b = next;
        }

        // Выводим пару чисел, дающую максимальное число шагов алгоритма Евклида
        std::cout << a << " " << b << "\n";
    }

    return 0;
}
