function matrixfy(str) {
  if (str.length === 0) {
    return 'name must be at least one letter';
  }
  const nextBiggestSquare = Math.ceil(Math.sqrt(str.length)) ** 2;
  const padded = str.padEnd(nextBiggestSquare, '.').split("");
  const matrix = [];
  const rowLength = Math.sqrt(nextBiggestSquare);
  for (let i = 0; i < rowLength; i++) {
    const row = [];
    for (let j = 0; j < rowLength; j++) {
      const next = padded.shift();
      row.push(next);
    }
    matrix.push(row);
  }
  return matrix;
}