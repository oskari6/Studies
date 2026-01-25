#include <iostream>
#include <vector>
using namespace std;

// nums1 has size m + n, with last n empty
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
  int i = m - 1;
  int j = n - 1;
  int k = m + n - 1;

  while (i >= 0 && j >= 0) {
    if (nums1[i] > nums2[j]) {
      nums1[k--] = nums1[i--];
    } else {
      nums1[k--] = nums2[j--];
    }
  }

  while (j >= 0) {
    nums1[k--] = nums2[j--];
  }
}

// So you don’t overwrite values you still need.
int main() {
  vector<int> nums1 = {1, 4, 7, 0, 0, 0};
  vector<int> nums2 = {2, 3, 5};

  merge(nums1, 3, nums2, 3);
  for (int item : nums1) {
    cout << item << " ";
  }
}