const doubleOrNothing = (cash, wager, losses) => {
  cash -= wager;
  while (--losses) {
    cash -= wager;
    wager *= 2;
  }
  return cash >= 0 ? cash : "I'll pay you back later";
};
