const getRealFloor = n => {
  if (n < 1) {
    return n;
  } else if (n < 13) {
    return n - 1;
  }
  return n - 2;
};