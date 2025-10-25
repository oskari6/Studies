#include <iostream>
#include <vector>

using namespace std;

int main() {
  unsigned long long x;
  cin >> x;
  vector<long long> arr(x);

  for (long long i = 0; i < x; i++) {
    cin >> arr[i];
  }

  long long total = 0;
  for (long long i = 1; i < x; i++) {
    if (arr[i] < arr[i - 1]) {
      total += arr[i - 1] - arr[i];
      arr[i] = arr[i - 1];
    }
  }
  cout << total;
}