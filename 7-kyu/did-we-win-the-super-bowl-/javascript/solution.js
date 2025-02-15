const didWeWin = plays => {
  let yardageGained = 0;
  for (const play of plays) {
    if (play.length !== 2) {
      break;
    } else if (play[1] === "turnover") {
      return false;
    } else if (play[1] === "sack") {
      yardageGained -= play[0];
    } else if (["run", "pass"].some(p => p === play[1])) {
      yardageGained += play[0];
    }
  }
  return yardageGained > 10;
};
