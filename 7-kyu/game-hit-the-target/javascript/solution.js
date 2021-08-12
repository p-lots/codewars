const solution = mtrx => {
  for (const row of mtrx) {
    if (row.includes('>') && row.includes('x')) {
      return row.indexOf('>') < row.indexOf('x');
    }
  }
  return false;
}