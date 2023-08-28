const isValidChess960 = (pieces) => {
  const leftBishop = pieces.indexOf("B");
  const rightBishop = pieces.lastIndexOf("B");
  const leftRook = pieces.indexOf("R");
  const rightRook = pieces.lastIndexOf("R");
  const king = pieces.indexOf("K");
  const bishopsCorrect = (leftBishop + rightBishop) % 2 === 1;
  const kingAndRooksCorrect = leftRook < king && king < rightRook;
  return bishopsCorrect && kingAndRooksCorrect;
};
