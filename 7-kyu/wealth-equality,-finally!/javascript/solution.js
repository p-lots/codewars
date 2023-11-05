const redistributeWealth = (wealth) => {
  const average = wealth.reduce((acc, nxt) => acc + nxt, 0) / wealth.length;
  for (let i = 0; i < wealth.length; i++) {
    wealth[i] = average;
  }
}