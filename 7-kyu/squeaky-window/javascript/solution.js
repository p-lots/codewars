function sliding(nums, k) {
  const maxs = [];
  for (let i = 0; i <= nums.length - k; i += k) {
    for (let j = i; j < i + k; j++) {
      const window = nums.slice(j, j + k);
      if (window.length < k) {
        continue;
      }
      const greatest = Math.max(...window);
      maxs.push(greatest);
    }
  }
  return maxs;
}