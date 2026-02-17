function fifa(ticket, results) {
  const ticketEntries = Object.entries(ticket);
  let totalWon = 0;
  for (let i = 0; i < 3; i++) {
    const [homeScore, awayScore] = results[i].split("-").map(score => Number(score));
    const potentialWinnings = Number(ticketEntries[i][1].slice(1));
    if (homeScore === awayScore && ticketEntries[i][0] === "Draw") {
      totalWon += potentialWinnings;
    } else if (awayScore > homeScore && ticketEntries[i][0] === "Away") {
      totalWon += potentialWinnings;
    } else if (homeScore > awayScore && ticketEntries[i][0] === "Home") {
      totalWon += potentialWinnings;
    }
  }
  return `£${totalWon}`;
}