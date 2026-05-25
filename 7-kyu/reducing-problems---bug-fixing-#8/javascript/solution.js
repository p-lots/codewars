const calculateTotal = (team1, team2) => {
  if (team1.length === 0 || team2.length === 0) {
    return team1.length > team2.length;
  }
  let team1sum = team1.reduce((t, c) => t + c);
  let team2sum = team2.reduce((t, c) => t + c);
  return team1sum > team2sum;
}