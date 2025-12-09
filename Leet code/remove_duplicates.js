var removeDuplicates = function (nums) {
  if (nums.length === 0) return 0;

  let uniqueIndex = 0; // Pointer for the last unique element.

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[uniqueIndex]) {
      uniqueIndex++;
      nums[uniqueIndex] = nums[i];
    }
  }

  return uniqueIndex + 1; // Length of the array without duplicates.
};
