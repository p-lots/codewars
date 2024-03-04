const minValue = values => {
  const valuesSet = new Set(values);
  const valuesArr = Array.from(valuesSet);
  return valuesArr.sort((a, b) => a - b).reduce((acc, nxt) => acc * 10 + nxt, 0);
};
