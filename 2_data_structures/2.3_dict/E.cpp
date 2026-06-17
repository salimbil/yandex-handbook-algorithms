// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    // Считаем количество вхождений каждого полного слова
    unordered_map<string, int> word_counts;
    vector<string> words(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> words[i];
        word_counts[words[i]]++;
    }
    
    if (words.empty()) {
        cout << 0 << "\n";
        return 0;
    }
    
    int len = words[0].length();
    
    // Массив хэш-таблиц: для каждой позиции i храним маску (слово без i-го символа) и её частоту
    vector<unordered_map<string, long long>> mask_maps(len);
    
    // Заполняем маски для всех уникальных слов с учетом их реальной частоты
    for (auto const& [word, count] : word_counts) {
        for (int i = 0; i < len; ++i) {
            // Формируем маску, исключая i-й символ
            string mask = word.substr(0, i) + word.substr(i + 1);
            mask_maps[i][mask] += count;
        }
    }
    
    long long total_interesting_pairs = 0;
    
    // Для каждого уникального слова считаем, с какими другими словами оно образует интересную пару
    for (auto const& [word, count] : word_counts) {
        long long current_word_pairs = 0;
        for (int i = 0; i < len; ++i) {
            string mask = word.substr(0, i) + word.substr(i + 1);
            // Всего слов с такой маской
            long long total_with_mask = mask_maps[i][mask];
            // Вычитаем количество копий точно такого же слова, чтобы убрать отличия в 0 букв
            current_word_pairs += (total_with_mask - count);
        }
        // Умножаем на количество вхождений текущего слова
        total_interesting_pairs += current_word_pairs * count;
    }
    
    // Так как каждую пару (A, B) мы посчитали и со стороны A, и со стороны B, делим на 2
    cout << total_interesting_pairs / 2 << "\n";
    
    return 0;
}
