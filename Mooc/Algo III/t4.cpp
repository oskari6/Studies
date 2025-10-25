#include <iostream>
#include <vector>

using namespace std;

int main() {
  long long n;
  cin >> n;
  vector<long long> arr(n);
  for (long long i = 0; i < n; i++) {
    cin >> arr[i];
  }
  vector<long long> position(n + 1);

  for (long long i = 0; i < n; i++) {
    position[arr[i]] = i;
  }

  long long total = 1;
  for (long long i = 1; i < n; i++) {
    if (position[i + 1] < position[i]) {
      total++;
    }
  }
  cout << total;
}