const rankOfElement = (arr, i) => {
  return arr.map((el, idx) => idx < i ? el <= arr[i] : el < arr[i]).reduce((acc, nxt) => acc + nxt, 0);
};
