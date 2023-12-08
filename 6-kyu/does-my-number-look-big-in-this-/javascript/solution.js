const narcissistic = value => {
  const valueStr = value.toString();
  let sum = 0;
  for (const digit of valueStr) {
    const digitNum = Number(digit);
    sum += digitNum ** valueStr.length;
  }
  return sum == value;
};
