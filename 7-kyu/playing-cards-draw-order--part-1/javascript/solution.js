const draw = (deck) => {
	let drawnCards = [];
  let i = 0;
  while (deck.length > 0) {
    const topCard = deck.shift();
    if (i % 2 === 0) {
      drawnCards.push(topCard);
    } else {
      deck.push(topCard);
    }
    i++;
  }
  return drawnCards;
};
