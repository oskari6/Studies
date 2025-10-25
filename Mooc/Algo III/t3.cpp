#include <iostream>
#include <vector>

using namespace std;

int main() {
  long long x;
  cin >> x;
  long long total = 0;
  for (long long i = 0; i < x; i++) {
    total += i + 1;
  }

  if (total % 2 == 0) {
    cout << "YES\n";
    vector<long long> set1, set2;

    long long sum = 0;
    for (long long i = x; i > 0; i--) {
      if (sum + i <= total / 2) {
        set1.push_back(i);
        sum += i;
      } else {
        set2.push_back(i);
      }
    }
    cout << set1.size() << "\n";
    for (auto v : set1) {
      cout << v << " ";
    }
    cout << "\n";

    cout << set2.size() << "\n";
    for (auto v : set2) {
      cout << v << " ";
    }
  } else {
    cout << "NO";
  }
}