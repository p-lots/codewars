const consecutive = arr => {
  if (!arr || arr.length === 0) {
    return 0;
  }
  const start = Math.min(...arr);
  const end = Math.max(...arr);
  return Math.abs(arr.length - (end - start + 1));
};
