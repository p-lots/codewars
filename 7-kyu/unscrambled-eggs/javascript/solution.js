const unscrambleEggs = (word) => {
  const noEggs = word.split("egg");
  return noEggs.filter(w => w.length > 0).join("");
};
