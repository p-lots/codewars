const firstNonConsecutive = arr => {
  let counter = arr[0];
  for (const n of arr) {
    if (counter != n) {
      return n;
    }
    counter += 1;
  }
  return null;
}