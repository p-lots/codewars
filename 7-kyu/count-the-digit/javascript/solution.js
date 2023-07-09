const nbDig = (n, d) => {
  let numbers = [];
  for (let i = 0; i <= n; i++) {
    numbers.push(i * i);
  }
  let count = 0;
  for (const num of numbers) {
    const numStr = num.toString();
    for (const ch of numStr) {
      if (ch === d.toString()) {
        count++;
      }
    }
  }
  return count;
}