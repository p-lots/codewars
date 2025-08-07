const vampireTest = (a, b) => {
  let sorted = Math.abs(a).toString().concat(Math.abs(b).toString()).split("").sort((x, y) => x - y).join("");
  const productSorted = ((a * b).toString()).split("").sort((x, y) => x - y).join("");
  if (a < 0 || b < 0 && a * b < 0) {
    sorted = "-" + sorted;
  }
  return sorted === productSorted;
};
