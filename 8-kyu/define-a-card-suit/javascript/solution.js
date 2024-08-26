const defineSuit = card => {
  const suitLookup = {"♣": "clubs", "♠": "spades", "♦": "diamonds", "♥": "hearts"};
  return suitLookup[card[card.length - 1]];
};
