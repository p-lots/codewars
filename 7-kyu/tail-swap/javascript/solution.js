const tailSwap = arr => {
  const [first, second] = arr;
  const [firstPart1, firstPart2] = first.split(":");
  const [secondPart1, secondPart2] = second.split(":");
  return [`${firstPart1}:${secondPart2}`, `${secondPart1}:${firstPart2}`];
}