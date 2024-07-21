const warnTheSheep = (queue) => {
  const wolfIdx = queue.indexOf("wolf");
  return wolfIdx === queue.length - 1 ? "Pls go away and stop eating my sheep" : `Oi! Sheep number ${queue.length - wolfIdx - 1}! You are about to be eaten by a wolf!`;
}