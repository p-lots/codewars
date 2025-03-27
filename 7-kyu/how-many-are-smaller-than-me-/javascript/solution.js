const smaller = nums => nums.map((n, idx, arr) => arr.slice(idx).filter((num) => num < n).length);
