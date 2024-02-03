const isFlush = cards => {
  let ret = true;
  for (let i = 0; i < cards.length - 1; i++) {
    if (cards[i].slice(-1) !== cards[i + 1].slice(-1)) {
      ret = false;
    }
  }
  return ret;
};
