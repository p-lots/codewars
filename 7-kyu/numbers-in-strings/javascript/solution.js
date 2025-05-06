const solve = s => {
  const numbers = s.split(/[^0-9]/g)
    .map(group => Number(group));
  return Math.max(...numbers);
};
