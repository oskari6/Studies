/*
k=3
1234567
7654321
5674321
5671234
 */

var rotate = function (nums, k) {
  let n = nums.length;
  k = k % n;

  if (k === 0) return;

  reverse(nums, 0, n - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, n - 1);
};

function reverse(arr, start, end) {
  while (start < end) {
    let temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start++;
    end--;
  }
}
