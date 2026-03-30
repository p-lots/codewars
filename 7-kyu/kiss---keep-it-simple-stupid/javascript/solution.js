const isKiss = words => {
  const totalWords = words.split(" ").length;
  return words.split(" ").every(word => word.length <= totalWords) ? "Good work Joe!" : "Keep It Simple Stupid";
};
