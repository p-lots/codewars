const buy = (x, arr) => {
  if (arr.length < 2 || arr.reduce((acc, nxt) => acc + nxt, 0) < x) {
    return null;
  }
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (i != j && arr[i] + arr[j] == x) {
        return [i, j];
      }
    }
  }
  return null;
};
