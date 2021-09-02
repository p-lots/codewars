const lastSurvivor = (letters, coords) => {
  if (letters.length === 1) {
    return letters;
  }
  const toDelete = coords.shift();
  let next = letters.split('');
  next.splice(toDelete, 1);
  next = next.join('');
  return lastSurvivor(next, coords);
}