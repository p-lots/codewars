const sizeToNumber = size => {
  if (!(/^x*[sl]$/g.test(size) || /^m$/g.test(size))) {
    return null;
  }
  const xModifier = 2;
  const xCount = [...size].filter((ch) => ch === "x").length * xModifier;
  const mediumBase = 38;
  const smallBase = 36;
  const largeBase = 40;
  if (size === "m") {
    return mediumBase;
  } else if (size.includes("s")) {
    return smallBase - xCount;
  }
  return largeBase + xCount;
};
