const rpsls = (player1, player2) => {
  const lookup = {"scissors": ["paper", "lizard"], "paper": ["rock", "spock"],
                  "rock": ["lizard", "scissors"], "lizard": ["spock", "paper"],
                  "spock": ["scissors", "rock"]
                 };
  if (lookup[player1].includes(player2)) {
    return "Player 1 Won!";
  } else if (lookup[player2].includes(player1)) {
    return "Player 2 Won!";
  }
  return "Draw!";
};
