const transposeTwoStrings = (array) => {
  let [left, right] = array;
  while (left.length < right.length) {
    left += " ";
  }
  while (right.length < left.length) {
    right += " ";
  }
  return [...left].map((elem, idx) => `${elem} ${right[idx]}`).join("\n");
};
