const arrayLeaders = numbers => {
  let sums = [];
  for (let i = 1; i <= numbers.length; i++) {
    sums.push(numbers.slice(i).reduce((acc, nxt) => acc + nxt, 0));
  }
  return numbers.filter((elem, idx) => sums[idx] < elem);
};
