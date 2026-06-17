// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Размер массива счетчиков (a_i <= 10^5)
const int MAX_VAL = 100005;
int counts[MAX_VAL];

struct Element {
    int value;
    int freq;
};

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    // Подсчитываем частоту каждого числа
    for (int i = 0; i < n; ++i) {
        int val;
        cin >> val;
        if (val < MAX_VAL) {
            counts[val]++;
        }
    }
    
    // Собираем все уникальные элементы, которые встретились хотя бы раз
    vector<Element> unique_elements;
    for (int i = 1; i < MAX_VAL; ++i) {
        if (counts[i] > 0) {
            unique_elements.push_back({i, counts[i]});
        }
    }
    
    // Сортируем: сначала по убыванию частоты, при равенстве — по возрастанию значения
    sort(unique_elements.begin(), unique_elements.end(), [](const Element& a, const Element& b) {
        if (a.freq != b.freq) {
            return a.freq > b.freq; // Чем больше частота, тем выше элемент
        }
        return a.value < b.value;   // При равной частоте берем меньшее значение
    });
    
    // Берем первые 3 лучших элемента
    vector<int> ans = {unique_elements[0].value, unique_elements[1].value, unique_elements[2].value};
    
    // По условию вывода тройку нужно вывести в порядке возрастания самих чисел
    sort(ans.begin(), ans.end());
    
    cout << ans[0] << " " << ans[1] << " " << ans[2] << "\n";
    
    return 0;
}
