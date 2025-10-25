#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  string word;
  cin >> word;
  sort(word.begin(), word.end());
  vector<string> words;

  do {
    words.push_back(word);
  } while (next_permutation(word.begin(), word.end()));

  cout << words.size() << "\n";
  for (auto &word : words) {
    cout << word << "\n";
  }
}