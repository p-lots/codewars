const intDiff = (arr, n) => {
  let ret = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (Math.abs(arr[i] - arr[j]) === n) {
        ret += 1;
      }
    }
  }
  return ret;
};
