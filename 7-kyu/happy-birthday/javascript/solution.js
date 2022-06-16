const wrap = (height, width, length) => {
  const [short, med, long] = [height, width, length].sort((a, b) => a - b);
  return 20 + (med * 2 + short * 2) + (long * 2 + short * 2);
};
