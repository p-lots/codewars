const jumpingNumber = n => {
  if (n < 10) {
    return "Jumping!!";
  }
  const nStr = n.toString();
  for (let i = 0; i < nStr.length - 1; i++) {
    if (Math.abs(Number(nStr[i]) - Number(nStr[i + 1])) !== 1) {
      return "Not!!";
    }
  }
  return "Jumping!!";
};
