const dominator = arr => {
  const counts = new Map();
  for (const num of arr) {
    if (!counts.has(num)) {
      counts.set(num, 1);
    } else {
      const currCount = counts.get(num);
      counts.set(num, currCount + 1);
    }
  }
  for (const [num, count] of counts) {
    if (count > arr.length / 2) {
      return num;
    }
  }
  return -1;
};
