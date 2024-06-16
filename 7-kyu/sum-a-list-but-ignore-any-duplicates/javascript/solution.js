const sumNoDuplicates = numList => {
  if (numList.length === 0) {
    return 0;
  }
  let numCounts = {};
  for (const num of numList) {
    if (!numCounts.hasOwnProperty(num)) {
      numCounts[num] = 1;
    } else {
      numCounts[num] += 1;
    }
  }
  let sum = 0;
  for (const num of numList) {
    if (numCounts[num] === 1) {
      sum += num;
    }
  }
  return sum;
};
