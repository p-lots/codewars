const digitsAverage = input => {
  if (input < 10) {
    return input;
  }
  const digits = input.toString().split("").map(Number);
  const next = [];
  for (let i = 0; i < digits.length - 1; i++) {
    const pair = [digits[i], digits[i + 1]];
    const sum = pair.reduce((acc, nxt) => acc + nxt, 0);
    const avg = Math.ceil(sum / 2);
    next.push(avg);
  }
  const nextNum = next.reduce((acc, nxt) => acc * 10 + nxt, 0);
  return digitsAverage(nextNum);
};
