const roundToNext5 = n => {
  let i = n;
  for (; i % 5 !== 0; i++) { }
  return i;
};
