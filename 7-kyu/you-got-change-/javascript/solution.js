const giveChange = amount => {
  const billAmounts = [100, 50, 20, 10, 5, 1];
  let ret = [0, 0, 0, 0, 0, 0];
  let retIdx = ret.length - 1;
  for (const bill of billAmounts) {
    while (amount >= bill) {
      amount -= bill;
      ret[retIdx]++;
    }
    retIdx--;
  }
  return ret;
};
