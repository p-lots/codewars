const highAndLow = numbers => {
  numbers = numbers.split(" ").map(elem => parseInt(elem));
  return `${Math.max(...numbers)} ${Math.min(...numbers)}`;
}