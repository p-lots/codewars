const tidyNumber = n => {
  const nSplit = n.toString().split("");
  for (let i = 0; i < nSplit.length - 1; i++) {
    if (nSplit[i + 1] < nSplit[i]) {
      return false;
    }
  }
  return true;
};