const newAvg = (arr, newavg) => {
  const ret = Math.ceil(newavg * (arr.length + 1) - arr.reduce((acc, nxt) => acc + nxt, 0));
  if (ret <= 0) {
    throw "Error: last donation is non-positive";
  }
  return ret;
};