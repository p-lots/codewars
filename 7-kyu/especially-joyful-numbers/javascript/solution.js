const numberJoy = n => {
  const digitSum = n.toString().split("").map(num => parseInt(num)).reduce((acc, nxt) => acc + nxt, 0);
  const digitSumReversed = parseInt(digitSum.toString().split("").reverse().join(""));
  return digitSum * digitSumReversed === n;
};
