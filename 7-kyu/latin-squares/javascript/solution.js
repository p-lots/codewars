const makeLatinSquare = (n) => {
  const latinSquare = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      const number = (i + j) % n + 1;
      row.push(number);
    }
    latinSquare.push(row);
  }
  return latinSquare;
};
