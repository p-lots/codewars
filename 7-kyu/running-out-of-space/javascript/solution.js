const spacey = array => {
  const decreasingSpace = [];
  for (let i = 0; i < array.length; i++) {
    const part = array.slice(0, i + 1)
      .join("");
    decreasingSpace.push(part);
  }
  return decreasingSpace;
};
