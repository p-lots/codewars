const getMatrix = (number) => {
  return Array.from({ length: number }, (elem, i) => {
    return Array.from({ length: number }, (el, j) => {
      return i === j ? 1 : 0;
    });
  });
};
