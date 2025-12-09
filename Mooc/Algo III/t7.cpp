#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<long long> coins(n);

  for (int i = 0; i < n; i++) {
    cin >> coins[i];
  }
  sort(coins.begin(), coins.end());

  long long best = 0;
  for (auto c : coins) {
    if (c > best + 1) {
      break;
    }
    best += c;
  }
  cout << best + 1;
}