const balance = (left, right) => {
  const count = (str, toCount) => [...str].filter(elem => elem === toCount).length;
  const leftCount = count(left, "!") * 2 + count(left, "?") * 3;
  const rightCount = count(right, "!") * 2 + count(right, "?") * 3;
  return leftCount > rightCount ? "Left" : leftCount === rightCount ? "Balance" : "Right";
};
