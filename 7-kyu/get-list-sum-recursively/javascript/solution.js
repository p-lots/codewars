const sumR = (x) => {
  return x.length === 0 ? 0 : x[0] + sumR(x.splice(1));
};