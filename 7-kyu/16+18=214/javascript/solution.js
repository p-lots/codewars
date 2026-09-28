const add = (num1, num2) => {
  let smaller = Math.min(num1, num2).toString();
  const larger = Math.max(num1, num2).toString();
  if (smaller.length < larger.length) {
    smaller = smaller.padStart(larger.length, "0");
  }
  let total = "";
  for (let i = 0; i < smaller.length; i++) {
    const digitTotal = String(Number(smaller[i]) + Number(larger[i]));
    total += digitTotal;
  }
  return Number(total);
};
