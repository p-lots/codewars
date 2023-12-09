const findUniq = arr => {
  const counts = new Map();
  for (const value of arr) {
    if (!counts.has(value)) {
      counts.set(value, 1);
    } else {
      const curr = counts.get(value);
      counts.set(value, curr + 1);
    }
  }
  for (const [key, value] of counts) {
    if (value === 1) {
      return key;
    }
  }
};
