const rps = (p1, p2) => {
  const losers = { scissors: "rock", rock: "paper", paper: "scissors" };
  if (losers[p1] === p2) {
    return "Player 2 won!";
  } else if (losers[p2] === p1) {
    return "Player 1 won!";
  }
  return "Draw!";
};