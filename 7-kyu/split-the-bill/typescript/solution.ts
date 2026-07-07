export function splitTheBill(x: {[k: string]: number}): {[k: string]: number} {
  const total = Object.values(x).reduce((acc, nxt) => acc + nxt, 0);
  const guests = Object.values(x).length;
  let ret: {[k: string]: number} = {};
  for (const key of Object.keys(x)) {
    const calcAmt = x[key] - total / guests;
    ret[key] = +(calcAmt.toFixed(2));
  }
  return ret;
}