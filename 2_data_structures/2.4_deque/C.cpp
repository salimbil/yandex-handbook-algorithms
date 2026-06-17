// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, k;
    if (!(cin >> n >> k)) return 0;
    
    // Очередь с приоритетами (min-heap) для хранения состояния серверов.
    // Хранит пары: {время_готовности, индекс_сервера}
    // Используем std::greater, чтобы на вершине всегда был минимальный элемент
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> servers;
    
    // Изначально все k серверов свободны с момента времени 0
    for (int i = 1; i <= k; ++i) {
        servers.push({0, i});
    }
    
    // Обрабатываем n пакетов
    for (int i = 0; i < n; ++i) {
        long long t, d;
        cin >> t >> d;
        
        // Извлекаем сервер с наименьшим временем готовности (и наименьшим ID при равенстве)
        auto [ready_time, server_id] = servers.top();
        servers.pop();
        
        long long completion_time;
        // Если сервер свободен к моменту прихода пакета, обработка начинается сразу в t
        if (ready_time <= t) {
            completion_time = t + d;
        } else {
            // Иначе пакет ждет своей очереди и обрабатывается сразу после готовности сервера
            completion_time = ready_time + d;
        }
        
        // Выводим время завершения текущего пакета
        cout << completion_time << (i == n - 1 ? "" : " ");
        
        // Возвращаем обновленный сервер обратно в кучу с новым временем готовности
        servers.push({completion_time, server_id});
    }
    cout << "\n";
    
    return 0;
}
