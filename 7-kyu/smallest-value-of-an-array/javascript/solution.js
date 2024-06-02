const min = (arr, toReturn) => {
  const minVal = Math.min(...arr);
  const minIdx = arr.indexOf(minVal);
  return toReturn === 'index' ? minIdx : minVal;
};
