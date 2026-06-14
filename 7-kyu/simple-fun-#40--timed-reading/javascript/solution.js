const timedReading = (maxLength, text) => {
  const words = text.split(" ").map((word) => word.replace(/[^\w]/g, ""));
  return words.filter((word) => word.length && word.length <= maxLength).length;
};
