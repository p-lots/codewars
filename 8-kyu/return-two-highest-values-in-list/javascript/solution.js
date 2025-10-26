const twoHighest = arr => {
  arr.sort((a, b) => b - a);
  const arrSet = new Set(arr);
  return Array.from(arrSet).slice(0, 2);
}