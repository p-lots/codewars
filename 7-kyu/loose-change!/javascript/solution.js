const changeCount = change => {
  const totalCents = change.split(" ").map(coin => CHANGE[coin]).reduce((acc, nxt) => acc + nxt * 100, 0);
  const dollarsAndCents = `$${totalCents / 100}`;
  const totalSplit = dollarsAndCents.split(".");
  if (totalSplit.length === 1) {
    return dollarsAndCents + ".00";
  }
  const cents = totalSplit[1];
  if (cents.length === 2) {
    return dollarsAndCents;
  }
  const centsPadded = cents.padEnd(2, "0");
  return dollarsAndCents.replace(/\d?$/, centsPadded);
};
