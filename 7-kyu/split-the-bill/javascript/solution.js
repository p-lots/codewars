const splitTheBill = x => {
  const billTotal = Object.values(x).reduce((acc, nxt) => acc + nxt, 0);
  const numGuests = Object.values(x).length;
  let ret = {};
  for (const k of Object.keys(x)) {
    const calculatedAmt = x[k] - billTotal / numGuests;
    ret[k] = +(calculatedAmt.toFixed(2));
  }
  return ret;
};
