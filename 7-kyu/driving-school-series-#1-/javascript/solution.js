const passed = (list) => {
  const passingScores = list.filter(score => score <= 18);
  if (passingScores.length === 0) {
    return "No pass scores registered.";
  }
  const average = passingScores.reduce((acc, nxt) => acc + nxt, 0) / passingScores.length;
  return Math.round(average);
};
