const scoreboard = str => {
  const score = [];
  const callouts = ["nil", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  for (const word of str.split(" ")) {
    if (callouts.includes(word)) {
      const idx = callouts.indexOf(word);
      score.push(idx);
    }
  }
  return score;
};
