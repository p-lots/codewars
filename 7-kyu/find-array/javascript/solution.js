const findArray = (arr1, arr2) => {
  const indices = arr2.filter(index => index < arr1.length);
  const foundArray = indices.map(idx => arr1[idx]);
  return foundArray;
};
