const howManyGifts = (maxBudget, gifts) => {
  if (maxBudget >= gifts.reduce((acc, nxt) => acc + nxt, 0)) {
    return gifts.length;
  }
  let numberOfGifts = 0;
  const giftsSorted = gifts.sort((a, b) => a - b);
  let runningTotal = giftsSorted[0];
  for (let i = 1; i < giftsSorted.length; i++) {
    if (runningTotal < maxBudget) {
      runningTotal += giftsSorted[i];
      numberOfGifts++;
    } else {
      break;
    }
  }
  return numberOfGifts;
};
