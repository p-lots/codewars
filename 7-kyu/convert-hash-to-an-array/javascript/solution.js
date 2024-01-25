function convertHashToArray(hash) {
  const hashEntries = Object.entries(hash);
    
  return hashEntries.sort((a, b) => {
    const lhs = a[0];
    const rhs = b[0];
    if (lhs < rhs) {
      return -1;
    } else if (lhs > rhs) {
      return 1;
    }
    return 0;
  });
}