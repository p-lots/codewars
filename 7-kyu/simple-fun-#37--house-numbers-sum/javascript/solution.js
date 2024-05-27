const houseNumbersSum = (inputArray) => {
  const zeroIdx = inputArray.indexOf(0);
  return inputArray.slice(0, zeroIdx).reduce((acc, nxt) => acc + nxt, 0);
};
