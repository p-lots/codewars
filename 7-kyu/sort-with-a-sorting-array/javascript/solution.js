const sort = (initialArray, sortingArray) => {
  const sortedArray = initialArray.map((elem) => elem);
  let i = 0;
  sortingArray.forEach((idx) => sortedArray[idx] = initialArray[i++]);
  return sortedArray;
};
