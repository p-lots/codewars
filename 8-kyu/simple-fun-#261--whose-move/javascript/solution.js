const whoseMove = (lastPlayer, win) => {
  if (win) {
    return lastPlayer;
  }
  return lastPlayer === "white" ? "black" : "white";
};
