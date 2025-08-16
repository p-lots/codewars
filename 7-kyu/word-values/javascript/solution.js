const wordValue = a => {
  const alphaLower = "abcdefghijklmnopqrstuvwxyz";
  return a.map((phrase, idx) => {
    return (idx + 1) * phrase.split(" ")
      .map(word => word.split("")
        .map(letter => alphaLower.indexOf(letter) + 1)
        .reduce((ac, nx) => ac + nx, 0)
      )
      .reduce((acc, nxt) => acc + nxt, 0);
  });
};
