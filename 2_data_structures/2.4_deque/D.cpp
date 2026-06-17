// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <string>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    string s;
    cin >> s;
    
    int left = 0;
    int right = n - 1;
    
    string result = "";
    result.reserve(n); // Резервируем память для скорости
    
    while (left <= right) {
        if (s[left] < s[right]) {
            result.push_back(s[left]);
            left++;
        } else if (s[left] > s[right]) {
            result.push_back(s[right]);
            right--;
        } else {
            // Если буквы с обеих сторон равны, по примечанию ВСЕГДА выбираем левую
            result.push_back(s[left]);
            left++;
        }
    }
    
    cout << result << "\n";
    
    return 0;
}
