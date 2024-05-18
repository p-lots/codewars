const removeSmallest = (numbers) => {
  let ret = numbers.map(n => n);
  const smallest = Math.min(...ret);
  const smallestIdx = ret.indexOf(smallest);
  ret.splice(smallestIdx, 1);
  return ret;
};
