const getLosAngelesPoints = results => {
  const LATeam = /^Los Angeles [A-Z][a-z]+$/;
  let totalPoints = 0;
  for (const [team, scoreline] of results) {
    if (LATeam.test(team)) {
      const [scored, _] = scoreline.split(":").map(Number);
      totalPoints += scored;
    }
  }
  return totalPoints;
};
