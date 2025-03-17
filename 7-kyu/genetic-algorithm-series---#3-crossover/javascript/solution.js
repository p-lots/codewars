const crossover = (chromosome1, chromosome2, index) => {
  const newChromosome1 = chromosome1.slice(0, index) + chromosome2.slice(index);
  const newChromosome2 = chromosome2.slice(0, index) + chromosome1.slice(index);
  return [newChromosome1, newChromosome2];
};
