const digits = n => {
  const nStr = n.toString()
  const sums = [];
  for (let i = 0; i < nStr.length; i++) {
    for (let j = i + 1; j < nStr.length; j++) {
      const sum = Number(nStr[i]) + Number(nStr[j]);
      sums.push(sum);
    }
  }
  return sums;
};
