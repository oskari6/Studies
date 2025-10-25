#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  queue<int> q;

  for (int i = 1; i <= n; i++) {
    q.push(i);
  }

  vector<int> order;
  while (!q.empty()) {
    q.push(q.front());
    q.pop();
    order.push_back(q.front());
    q.pop();
  }
  for (int x : order) {
    cout << x << " ";
  }
}