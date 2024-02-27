const findNextSquare = (sq) => {
  // Return the next square if sq is a perfect square, -1 otherwise
  const root = Math.sqrt(sq);
  if (Math.floor(root) * Math.floor(root) !== sq) {
    return -1;
  }
  return (root + 1) ** 2;
};
