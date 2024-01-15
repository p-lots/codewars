const calc = (x) => {
  const total1 = [...x].map((elem) => elem.charCodeAt(0)).join("");
  const total2 = total1.replace(/7/g, "1");
  const total1DigitSum = [...total1].map((elem) => parseInt(elem)).reduce((acc, nxt) => acc + nxt, 0);
  const total2DigitSum = [...total2].map((elem) => parseInt(elem)).reduce((acc, nxt) => acc + nxt, 0);
  return total1DigitSum - total2DigitSum;
};
