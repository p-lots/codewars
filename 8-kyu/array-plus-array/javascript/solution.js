const arrayPlusArray = (arr1, arr2) => {
  const ret = arr1.concat(arr2);
  return ret.reduce((acc, nxt) => acc + nxt, 0);
};
