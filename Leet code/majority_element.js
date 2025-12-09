//Boyer Moore Voting Algorithm
var mahorityElement = function (nums) {
  let candidate = null;
  let count = 0;

  //find candidate
  for (let num of nums) {
    if (count === 0) {
      candidate = num;
    }
    count += num === candidate ? 1 : -1;
  }

  // Verify candidate, optional to assume there always is majority candidate
  count = 0;
  for (let num of nums) {
    if (num === candidate) {
      count++;
    }
  }
  return candidate;
};
