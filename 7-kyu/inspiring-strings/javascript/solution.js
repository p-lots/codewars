const longestWord = stringOfWords => {
  const lengths = stringOfWords.split(" ").map(word => word.length);
  const longest = Math.max(...lengths);
  return stringOfWords.split(" ").findLast(word => word.length >= longest);
}