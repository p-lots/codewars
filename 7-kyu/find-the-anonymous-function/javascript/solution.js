const FindFunction = (func, arr) => {
  const foundFunction = func.filter(f => typeof f === 'function')[0];
  return arr.filter(foundFunction);
};
