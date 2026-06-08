const isSantaClausable = obj => {
  const santaClausableProps = ["sayHoHoHo", "distributeGifts", "goDownTheChimney"];
  return santaClausableProps.every(prop => obj[prop] !== undefined && typeof obj[prop] === 'function');
};
