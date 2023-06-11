const findLongest = str => {
  const wordLengths = str.split(" ").map(word => word.length);
  return Math.max(...wordLengths);
};
