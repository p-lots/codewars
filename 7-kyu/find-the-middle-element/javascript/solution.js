const gimme = (triplet) => {
  const smallest = Math.min(...triplet);
  const largest = Math.max(...triplet);
  for (let i = 0; i < triplet.length; i++) {
    if (triplet[i] !== smallest && triplet[i] !== largest) {
      return i;
    }
  }
}