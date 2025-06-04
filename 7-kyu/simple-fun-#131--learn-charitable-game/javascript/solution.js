const learnCharitableGame = (arr) => {
  if (arr.every(amt => amt === 0) || arr.length === 0) {
    return false;
  }
  return arr.reduce((acc, nxt) => acc + nxt, 0) % arr.length === 0;
};
